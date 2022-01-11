#!/usr/bin/env python3
"""
Terminal program to show realtime info from De lijn. I wrote this thing because the official
(android) app works awfully slow on my phone. A solution is to make a terminal program with
(a lot) fewer features:

*   search realtime info for a specific bus stop. When there's no result search for
    a stop by name

*   Filter search results by line nr

For the gui I have used the urwid module.
There are Dutch words in the code and comments because I kept the same variable names as found in
the api from De Lijn.

used sources:
API https://delijn.docs.apiary.io/
urwid https://urwid.org

I've used the old api because the new one (https://data.delijn.be/) needs much more api calls and code.

Script flow:
    * Main menu:
        User info [optional]: search previous successful entry if present
        User input: haltenummer -> Doorkomsten | name -> Search halte | bookmark nr -> Doorkomsten
        Buttons: exit
        Output: bookmarks list

        * Search halte menu:
            User input: nr search result -> Doorkomsten
            Buttons: new search -> Main menu, exit
            Output: search results

        * Doorkomsten menu:
            User input: 'f' -> Doorkomsten(filter), 'enter' = refresh
            Buttons: new search -> Main menu, refresh, filter -> Filter menu | remove filter if filter is applied, exit
            Output: doorkomsten [optional filtered line] (autorefresh each n seconds)

        * Filter menu:
            User_info: possible line nrs to filter
            User input: line nr to filter -> Doorkomsten menu with filtered doorkomsten

# TODO parse info about delays/disruptions/detours
"""
# Postpone evaluation for type annonations https://www.python.org/dev/peps/pep-0563/
from __future__ import annotations

from enum import Enum
from signal import signal, SIGINT, SIGHUP
from datetime import datetime, timedelta
from typing import Optional

import urwid

import delijnapi
from tui import PALETTE, ICON
import bookmarks

QUERY_LOG = "search.txt"
BOOKMARKS = list(bookmarks.BOOKMARKS.items())
PROGRAM_TITLE = "\U0001F68B \U0001F68C \U0001F68B De lijn doorkomsten \U0001F68C \U0001F68B \U0001F68C"
DOORKOMSTEN_REFRESH = 60

UrwidText = list[tuple[str, str]]


class Output(urwid.Padding):
    """
    Packaging of the urwid objects.
    Methods control the appearance of the ui
    """

    def __init__(self, program: Program):
        self.program = program

        self.div = urwid.Divider(div_char='-')

        edit = urwid.Edit("")
        self.input_user = UserInput(edit, program, self)

        self.txt_output = urwid.Text("", align='left')  # TODO change to listbox
        self.txt_info = urwid.Text("")

        self.button_exit = urwid.Button("Afsluiten", on_press=exit_urwid)
        self.button_bookmarks = urwid.Button("Favorieten", on_press=button_bookmarks_handler, user_data=self)
        self.button_new_search = urwid.Button("Home", on_press=button_main_menu_handler, user_data=self)
        self.button_filter = urwid.Button("Filteren", on_press=button_filter_handler, user_data=self)
        self.button_remove_filter = urwid.Button("Verwijder filter", on_press=button_remove_filter_handler,
                                                 user_data=self)
        self.buttons = urwid.Columns([self.button_exit], dividechars=1, box_columns=[self.button_exit])

        self.pile = urwid.Pile([
            self.input_user,
            self.div,
            self.txt_output,
            self.div,
            ('pack', self.buttons)
        ], focus_item=0)

        self.main_filler = urwid.Filler(self.pile, valign='top')
        self.main_window = urwid.LineBox(urwid.Padding(self.main_filler, left=1), title=PROGRAM_TITLE)

        super().__init__(self.main_window)
        self.set_main_menu()

    def _set_buttons(self, buttons: list[urwid.Button]):
        new_buttons = [(btn, urwid.Columns.options('given', len(btn.label) + 4)) for btn in buttons]
        setattr(self.buttons, 'contents', new_buttons)
        setattr(self.buttons, 'box_buttons', buttons)

    def set_main_menu(self):
        self.input_user.original_widget.set_caption(('bold', "Geef haltenummer of zoekterm: "))
        self.input_user.original_widget.set_edit_text("")
        self.txt_output.set_text(get_bookmarks())
        self._set_buttons([
            self.button_bookmarks,
            self.button_exit
        ])

        if self.program.last_query:
            self.txt_info.set_text(f"Druk op enter om terug '{self.program.last_query}' op te zoeken")
            if self.txt_info not in [w[0] for w in self.pile.contents]:
                self.pile.widget_list.insert(0, self.txt_info)
            self.pile.focus_item = 1

    def set_search_halte_menu(self, search_result: UrwidText):
        keys = [key for key, _ in enumerate(search_result)]
        # first item in last_search is a summary line
        self.input_user.original_widget.set_caption(f"Kies een nr({min(keys) + 1}-{max(keys)}): ")
        self.txt_output.set_text(search_result)
        self._set_buttons([
            self.button_new_search,
            self.button_exit
        ])

        self.pile.contents = [w for w in self.pile.contents if w[0] != self.txt_info]
        setattr(self.pile, 'focus_position', 0)

    def set_doorkomsten_menu(self, doorkomsten: UrwidText):
        if self.program.line_filter:
            caption_text = "Druk 'f' om de filter te verwijderen. 'Enter' om te vernieuwen"
        elif len(get_lines_from_doorkomsten(self.program.last_doorkomsten)) == 1:
            caption_text = "Druk op 'Enter' om te vernieuwen"
        else:
            caption_text = "Druk 'f' om te filteren op lijn. 'Enter' om te vernieuwen"

        self.input_user.original_widget.set_caption(caption_text)
        self.txt_output.set_text(doorkomsten)
        buttons = [self.button_new_search, self.button_exit]
        lines = get_lines_from_doorkomsten(self.program.last_doorkomsten)
        if len(lines) > 1:
            buttons.insert(1, self.button_filter)
        elif self.program.line_filter:
            buttons.insert(1, self.button_remove_filter)

        self._set_buttons(buttons)
        self.pile.contents = [w for w in self.pile.contents if w[0] != self.txt_info]
        setattr(self.pile, 'focus_position', 0)

    def set_choose_line_filter_menu(self, lines: list[str]):
        self.input_user.original_widget.set_caption(f"Kies lijn nummer ({', '.join(lines)}): ")
        self._set_buttons([
            self.button_new_search,
            self.button_exit
        ])
        setattr(self.pile, 'focus_position', 0)

    def set_filtered_doorkomsten_menu(self, doorkomsten: UrwidText):
        self.txt_output.set_text(doorkomsten)
        self._set_buttons([
            self.button_new_search,
            self.button_remove_filter,
            self.button_exit
        ])


def doorkomsten_alarm_handler(_loop: urwid.MainLoop, output: Output):
    if output.program.state == States.DOORKOMSTEN_MENU:
        output.input_user.keypress((), 'enter')
    _loop.set_alarm_in(DOORKOMSTEN_REFRESH, doorkomsten_alarm_handler, user_data=output)


def button_bookmarks_handler(button: urwid.Button, out: Output) -> None:
    out.txt_output.set_text(get_bookmarks())


def button_main_menu_handler(button: urwid.Button, out: Output) -> None:
    out.program.state = States.MAIN
    out.program.last_search.clear()
    out.program.last_doorkomsten.clear()
    out.set_main_menu()


def button_filter_handler(button: urwid.Button, out: Output) -> None:
    out.program.line_filter = None
    lines = get_lines_from_doorkomsten(out.program.last_doorkomsten)
    out.set_choose_line_filter_menu(lines)


def button_remove_filter_handler(button: urwid.Button, out: Output) -> None:
    out.program.line_filter = None
    out.program.doorkomsten(out, out.program.last_doorkomsten['halteNummer'])


def exit_urwid(*args):
    raise urwid.ExitMainLoop()


def unhandled_input_handler(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def signal_handler(*args) -> None:
    """Handler for SIGINT signal"""
    exit_urwid("signal")


class Program:
    def __init__(self):
        self.state: States = States.MAIN
        self.last_query: str = get_last_query()
        self.last_doorkomsten: dict = {}
        self.last_search: dict = {}
        self.line_filter: str = str()

    def doorkomsten(self, out: Output, halte_nummer: int) -> None:
        """Process doorkomsten"""
        data = delijnapi.api_get_doorkomsten(halte_nummer)
        if data == 'timeout':
            out.txt_output.set_text(('red bold', "Couldn't reach api. Is there an internet connection?"))
            return

        try:
            self.last_doorkomsten = data['halte'][0]
            if self.line_filter:
                self.last_doorkomsten['lijnen'] = [item for item in self.last_doorkomsten['lijnen'] if
                                                   item['lijnNummerPubliek'] == self.line_filter]

            doorkomsten_output = get_doorkomsten_text(self.last_doorkomsten)
            out.set_doorkomsten_menu(doorkomsten_output)
            save_query(halte_nummer)
            self.last_query = str(halte_nummer)
            self.state = States.DOORKOMSTEN_MENU

        except IndexError:
            out.txt_output.set_text(('red bold', "Geen halte of doorkomsten rond huidig tijdstip gevonden"))

    def search_halte(self, out: Output, query: str) -> None:
        """Process halte search"""
        data = delijnapi.api_search_halte(query)
        if data is None:
            return

        if not data['haltes']:
            out.txt_output.set_text(('red bold', "\nNiets gevonden.probeer een andere zoekterm"))
        else:
            search_output = get_halte_search_results_text(data, query)
            out.set_search_halte_menu(search_output)
            save_query(query)
            self.last_query = str(query)
            self.state = States.SEARCH_HALTE_MENU
            self.last_search = data

    def process_userinput_main(self, out: Output, input_text: str):
        if input_text == '' and self.last_query:
            input_text = self.last_query

        if input_text.isdigit():
            halte_nr = int(input_text)
            if halte_nr - 1 in range(len(BOOKMARKS)):
                self.doorkomsten(out, BOOKMARKS[halte_nr - 1][1])
            else:
                self.doorkomsten(out, halte_nr)

        else:
            self.search_halte(out, input_text)

    def process_userinput_doorkomsten(self, out: Output, user_input: str):
        if user_input == 'enter':
            self.doorkomsten(out, int(self.last_query))
        elif user_input == 'f' and self.line_filter:
            self.line_filter = None
            self.doorkomsten(out, int(self.last_query))
        elif user_input == 'f':
            lines = get_lines_from_doorkomsten(self.last_doorkomsten)
            if len(lines) < 2:
                return

            out.set_choose_line_filter_menu(lines)
            self.state = States.FILTER_MENU

    def process_userinput_search_halte(self, out: Output, input_text: str):
        if input_text.isdigit() and int(input_text) - 1 in range(len(self.last_search['haltes'])):
            haltenr = self.last_search['haltes'][int(input_text) - 1]['halteNummer']
            self.doorkomsten(out, haltenr)
        else:
            text = [('red bold', f"Ongeldige invoer: \"{input_text}\"")] + \
                   get_halte_search_results_text(self.last_search, self.last_query)
            out.txt_output.set_text(text)

    def process_userinput_filter(self, out: Output, input_text: str):
        if input_text in get_lines_from_doorkomsten(self.last_doorkomsten):
            self.line_filter = input_text
            self.doorkomsten(out, self.last_doorkomsten['halteNummer'])
        else:
            text = [('red bold', f"Ongeldige invoer: \"{input_text}\"")] + get_doorkomsten_text(self.last_doorkomsten)
            out.txt_output.set_text(text)


class UserInput(urwid.Padding):
    """Handle user text input"""

    def __init__(self, user_input: urwid.Edit, program: Program, out: Output):
        self.program = program
        self.output = out
        super().__init__(user_input)

    def keypress(self, size: tuple, key: str) -> Optional[str]:
        """Select handler for keypress"""
        state = self.program.state
        if state == States.MAIN:
            return self._process_main(size, key)
        if state == States.DOORKOMSTEN_MENU:
            return self._process_doorkomsten(size, key)
        if state == States.SEARCH_HALTE_MENU:
            return self._process_search_halte(size, key)
        if state == States.FILTER_MENU:
            return self._process_filter(size, key)

    def _process_main(self, size: tuple, key: str) -> Optional[str]:
        """Handler for submit in main menu"""
        if key != 'enter':
            return super().keypress(size, key)

        self.program.process_userinput_main(self.output, self.original_widget.edit_text)
        return super().original_widget.set_edit_text("")

    def _process_doorkomsten(self, size: tuple, key: str) -> Optional[str]:
        """Handler for keypress in doorkomsten menu. (keypress here instead of submit)"""
        if key in ['f', 'enter']:
            self.program.process_userinput_doorkomsten(self.output, key)
            return super().original_widget.set_edit_text("")

        return super().keypress(size, key)

    def _process_search_halte(self, size: tuple, key: str):
        """Handler for submit in search halte menu."""
        if key != 'enter':
            return super().keypress(size, key)

        self.program.process_userinput_search_halte(self.output, self.original_widget.edit_text)
        return super().original_widget.set_edit_text("")

    def _process_filter(self, size: tuple, key: str):
        if key != 'enter':
            return super().keypress(size, key)

        self.program.process_userinput_filter(self.output, self.original_widget.edit_text)
        return super().original_widget.set_edit_text("")


def save_query(query_input: [str, int]) -> None:
    """Put search query in a text file"""
    with open(QUERY_LOG, "w", encoding="utf8") as file:
        file.write(str(query_input))


def get_last_query() -> str:
    """Read last search entry from text file"""
    try:
        with open(QUERY_LOG, "r", encoding="utf8") as file:
            return file.readline().rstrip()
    except FileNotFoundError:
        return ""


def get_lines_from_doorkomsten(doorkomsten: dict) -> list[str]:
    """Give a list containing the line nrs from the raw data returned by delijn api"""
    lines = [line['lijnNummerPubliek'] for line in doorkomsten['lijnen']]
    lines = list(dict.fromkeys(lines))
    lines.sort()
    return lines


def get_doorkomsten_text(doorkomsten: dict) -> UrwidText:
    """Fetch text with urwid markup, parsed from api_get_doorkomsten result"""
    text = [('lightcyan', f"\n{doorkomsten['omschrijvingLang']} - haltenr: {doorkomsten['halteNummer']}\n")]
    text_color = 'green'

    for item in doorkomsten['lijnen']:
        vertrektijd = datetime.fromtimestamp(item['vertrekTheoretischeTijdstip'] / 1000)
        vertrektijd_text = ""
        delay_text = None

        if "CANCELLED" in item['predictionStatussen'] or "DELETED" in item['predictionStatussen']:
            realtime_text = ('red', f'{"Rijdt niet":<7}')
        elif "REALTIME" in item['predictionStatussen']:
            realtime_text = (text_color, f"{item['vertrekTijd']:<7}")
            try:
                vertrektijd_rt = datetime.fromtimestamp(item['vertrekRealtimeTijdstip'] / 1000)
                vertrektijd_text = vertrektijd.strftime('%H:%M')
                if vertrektijd_rt > vertrektijd + timedelta(seconds=60):
                    delay = vertrektijd_rt - vertrektijd
                    delay_text = ('red', f"+{delay.seconds // 60}\'\n")
                elif vertrektijd_rt < vertrektijd - timedelta(seconds=60):
                    delay = vertrektijd - vertrektijd_rt
                    # add an extra min to increase chances of catching your bus...
                    delay_text = ('red', f"-{(delay.seconds // 60) + 1}\'\n")
            except TypeError:
                pass  # 'vertrekRealtimeTijdstip' = None (Sometimes, the api doesn't return the calculated ETA)
        else:
            realtime_text = (text_color, f'{"GN RT":<7}')
            vertrektijd_text = vertrektijd.strftime('%H:%M')

        icon = ICON.get(item['lijnType'], "")
        line = [
            (text_color, f"{icon} {item['lijnType']:<5}{item['lijnNummerPubliek']:<4}{item['bestemming']:<20}"),
            realtime_text,
            (text_color, f"{vertrektijd_text:<7}"),
            '\n' if delay_text is None else delay_text]

        text.extend(line)
        text_color = 'yellow' if text_color == 'green' else 'green'

    return text


def get_halte_search_results_text(results: dict, query: str) -> UrwidText:
    """Fetch text with urwid markup, parsed from 'api_search_halte' result"""
    haltes = results['haltes']
    text = [('lightcyan', f"\n\"{query}\": {len(results['haltes'])} resultaten\n")]
    text_color = 'green'

    for index, halte in enumerate(haltes):
        lijn_nummers = ", ".join([lijn['lijnNummerPubliek'] for lijn in halte['lijnen']])
        bestemmingen = ", ".join(halte['bestemmingen'])
        text.append((text_color, f"{index + 1}) {halte['omschrijvingLang']} - haltenr: "f"{halte['halteNummer']} - "
                                 f"Lijnen: {lijn_nummers} Richting: {bestemmingen}\n"))
        text_color = 'yellow' if text_color == 'green' else 'green'

    return text


def get_bookmarks() -> UrwidText:
    """Give text with urwid markup from bookmark list"""
    stop_length = max([len(stop) for stop, _ in BOOKMARKS])
    bookmark_text = ""
    for index, (stop, halte_nr) in enumerate(BOOKMARKS):
        index_text = f"{index + 1})"
        bookmark_text += f" {index_text:<4}{stop:<{stop_length}} ({halte_nr})\n"

    return [('lightcyan bold', "Favorieten\n"), ('lightcyan', bookmark_text)]


class States(Enum):
    MAIN = 0
    DOORKOMSTEN_MENU = 1
    SEARCH_HALTE_MENU = 2
    FILTER_MENU = 3


signal(SIGINT, signal_handler)
signal(SIGHUP, signal_handler)

prog = Program()
output = Output(prog)
loop = urwid.MainLoop(output.original_widget, unhandled_input=unhandled_input_handler, palette=PALETTE)
loop.set_alarm_in(DOORKOMSTEN_REFRESH, doorkomsten_alarm_handler, user_data=output)
loop.run()
