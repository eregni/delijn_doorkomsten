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

# todo parse info about delays/disruptions/detours
# todo packaging
"""
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

UrwidText = list[tuple[str, str]]


class Output(urwid.Padding):
    """
    Packaging of the urwid objects.
    Methods control the appearance of the ui
    """
    def __init__(self):
        self.div = urwid.Divider(div_char='-')

        edit = urwid.Edit("")
        self.input_user = UserInput(edit)

        self.txt_output = urwid.Text(u"", align='left')  # TODO change to listbox
        self.txt_info = urwid.Text(u"")
        self.txt_error = urwid.Text(u"")  # todo implement text object to display the errors

        self.button_exit = urwid.Button(u"Afsluiten", on_press=exit_urwid)
        self.button_bookmarks = urwid.Button(u"Favorieten", on_press=button_bookmarks_handler, user_data=self)
        self.button_new_search = urwid.Button(u"Nieuwe zoekopdracht", on_press=button_main_menu_handler, user_data=self)
        self.button_filter = urwid.Button(u"Filteren", on_press=button_filter_handler, user_data=self)
        self.button_remove_filter = urwid.Button(u"Filter verwijderen", on_press=button_remove_filter_handler,
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

        global last_query
        if last_query:
            self.txt_info.set_text(f"Druk op enter om terug '{last_query}' op te zoeken")
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

    def set_doorkomsten_menu(self, dk: UrwidText):
        global line_filter, last_doorkomsten
        if line_filter:
            caption_text = "Druk 'f' om te filter te verwijderen. 'Enter' om te vernieuwen"
        else:
            caption_text = "Druk 'f' om te filteren op lijn. 'Enter' om te vernieuwen"

        self.input_user.original_widget.set_caption(caption_text)
        self.txt_output.set_text(dk)
        buttons = [self.button_new_search, self.button_exit]
        lines = get_lines_from_doorkomsten(last_doorkomsten)
        if len(lines) > 1:
            buttons.insert(1, self.button_filter)
        elif line_filter:
            buttons.insert(1, self.button_remove_filter)

        self._set_buttons(buttons)
        self.pile.contents = [w for w in self.pile.contents if w[0] != self.txt_info]
        setattr(self.pile, 'focus_position', 0)

    def set_choose_line_filter(self, lines: list[str]):
        self.input_user.original_widget.set_caption(f"Kies lijn nummer ({', '.join(lines)}): ")
        buttons = [self.button_new_search, self.button_exit]
        self._set_buttons(buttons)
        setattr(self.pile, 'focus_position', 0)

    def set_filtered_doorkomsten_menu(self, dk: UrwidText):
        self.txt_output.set_text(dk)
        self._set_buttons([
            self.button_new_search,
            self.button_remove_filter,
            self.button_exit
        ])


def button_bookmarks_handler(button: urwid.Button, out: Output) -> None:
    out.txt_output.set_text(get_bookmarks())


def button_main_menu_handler(button: urwid.Button, out: Output):
    global state, last_search, last_query, last_doorkomsten
    state = States.main
    last_search.clear()
    last_doorkomsten.clear()
    out.set_main_menu()


def button_filter_handler(button: urwid.Button, out: Output) -> None:
    global last_doorkomsten, line_filter
    line_filter = None
    lines = get_lines_from_doorkomsten(last_doorkomsten)
    output.set_choose_line_filter(lines)


def button_remove_filter_handler(button: urwid.Button, out: Output) -> None:
    global last_doorkomsten, line_filter
    line_filter = None
    doorkomsten(out, last_doorkomsten['halteNummer'])


def exit_urwid(*args):
    raise urwid.ExitMainLoop()


def unhandled_input_handler(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def signal_handler(*args) -> None:
    """Handler for SIGINT signal"""
    exit_urwid("signal")


class UserInput(urwid.Padding):
    """Handle user text input"""
    def __init__(self, user_input: urwid.Edit):
        super().__init__(user_input)

    def keypress(self, size: tuple, key: str) -> Optional[str]:
        """Select handler for keypress"""
        global state
        if state == States.main:
            return self._process_main(size, key)
        elif state == States.doorkomsten_menu:
            return self._process_doorkomsten(size, key)
        elif state == States.search_halte_menu:
            return self._process_search_halte(size, key)
        elif state == States.filter_menu:
            return self._process_filter(size, key)

    def _process_main(self, size: tuple, key: str) -> Optional[str]:
        """Handler for keypress in main menu"""
        if key != 'enter':
            return super(UserInput, self).keypress(size, key)

        edit_text: str = self.original_widget.edit_text
        global last_query
        if edit_text == '' and last_query:
            edit_text = last_query

        if edit_text.isdigit():
            nr = int(edit_text)
            if nr - 1 in range(len(BOOKMARKS)):
                doorkomsten(output, BOOKMARKS[nr - 1][1])
            else:
                doorkomsten(output, nr)

        else:
            search_halte(output, edit_text)

        return super(UserInput, self).original_widget.set_edit_text("")

    def _process_doorkomsten(self, size: tuple, key: str) -> Optional[str]:
        """Handler for keypress in doorkomsten menu. Actions are triggered here by keypress instead of submit"""
        global state, last_doorkomsten, line_filter
        if key == 'enter' or (key == 'f' and line_filter):  #  todo check this logic (too late in the night to test. No more busses driving...)
            doorkomsten(output, int(last_query))
        elif key == 'f':
            lines = get_lines_from_doorkomsten(last_doorkomsten)
            if len(lines) < 2:
                return

            output.set_choose_line_filter(lines)
            state = States.filter_menu
        else:
            return super(UserInput, self).keypress(size, key)

    def _process_search_halte(self, size: tuple, key: str):
        """Handler for keypress in search halte menu."""
        if key != 'enter':
            return super(UserInput, self).keypress(size, key)

        edit_text: str = self.original_widget.edit_text
        global last_search
        if edit_text.isdigit() and int(edit_text) - 1 in range(len(last_search['haltes'])):
            haltenr = last_search['haltes'][int(edit_text) - 1]['halteNummer']
            doorkomsten(output, haltenr)
        else:
            text = [('red', f"Ongeldige invoer")] + get_doorkomsten_text(last_search)
            # todo what happens with the menu in case of doorkomsten exceptions? -> implement extra urwid Text object
            output.txt_output.set_text(text)

        return super(UserInput, self).original_widget.set_edit_text("")

    def _process_filter(self, size: tuple, key: str):
        if key != 'enter':
            return super(UserInput, self).keypress(size, key)

        global last_doorkomsten, line_filter
        lf = output.input_user.original_widget.edit_text
        if lf in get_lines_from_doorkomsten(last_doorkomsten):
            # todo  -> implement extra urwid Text object to display error 'invalid input'
            line_filter = lf
            doorkomsten(output, last_doorkomsten['halteNummer'], lf)

        return super(UserInput, self).original_widget.set_edit_text("")


def save_query(query_input: [str, int]) -> None:
    """Put search query in a text file"""
    global last_query
    last_query = str(query_input)
    with open(QUERY_LOG, "w") as file:
        file.write(str(last_query))


def get_last_query() -> str:
    """Read last search entry from text file"""
    try:
        with open(QUERY_LOG, "r") as file:
            return file.readline().rstrip()
    except FileNotFoundError:
        return ""


def get_lines_from_doorkomsten(dk: dict) -> list[str]:
    lines = [line['lijnNummerPubliek'] for line in dk['lijnen']]
    lines = list(dict.fromkeys(lines))
    lines.sort()
    return lines


def get_doorkomsten_text(dk: dict) -> UrwidText:
    """print parsed data in terminal"""
    text = [('lightcyan', f"\n{dk['omschrijvingLang']} - haltenr: {dk['halteNummer']}\n")]
    text_color = 'green'

    for item in dk['lijnen']:
        vertrektijd = datetime.fromtimestamp(item['vertrekTheoretischeTijdstip'] / 1000)
        vertrektijd_text = ""
        delay_text = None

        if "CANCELLED" in item['predictionStatussen'] or "DELETED" in item['predictionStatussen']:
            realtime_text = "Rijdt niet"
        elif "REALTIME" in item['predictionStatussen']:
            realtime_text = item['vertrekTijd']
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
            except TypeError:  # 'vertrekRealtimeTijdstip' = None (Sometimes, the api doesn't return the calculated ETA)
                pass
        else:
            realtime_text = "GN RT"
            vertrektijd_text = vertrektijd.strftime('%H:%M')

        icon = ICON.get(item['lijnType'], "")
        line = [(text_color,
                 f"{icon} {item['lijnType']:<5}{item['lijnNummerPubliek']:<4}{item['bestemming']:<20}{realtime_text:<7}"
                 f"{vertrektijd_text:<7}"),
                '\n' if delay_text is None else delay_text]

        text.extend(line)
        text_color = 'yellow' if text_color == 'green' else 'green'

    return text


def get_halte_search_results_text(results: dict, query: str) -> UrwidText:
    """Get text with urwid markup, parsed from 'api_search_halte' result"""
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
    """Give string + urwid markup from bookmark list"""
    stop_length = max([len(stop) for stop, _ in BOOKMARKS])
    bookmark_text = ""
    for index, (stop, nr) in enumerate(BOOKMARKS):
        index_text = f"{index + 1})"
        bookmark_text += f" {index_text:<4}{stop:<{stop_length}} ({nr})\n"

    return [('lightcyan bold', "Favorieten\n"), ('lightcyan', bookmark_text)]


def doorkomsten(out: Output, halte_nummer: int, linefilter: int = None) -> None:
    """Process the doorkomsten table"""
    global last_doorkomsten, state
    data = delijnapi.api_get_doorkomsten(halte_nummer)
    try:
        last_doorkomsten = data['halte'][0]
        if linefilter:
            last_doorkomsten['lijnen'] = [item for item in last_doorkomsten['lijnen'] if item['lijnNummerPubliek'] == linefilter]

        doorkomsten_output = get_doorkomsten_text(last_doorkomsten)
        out.set_doorkomsten_menu(doorkomsten_output)
        save_query(halte_nummer)
        state = States.doorkomsten_menu
    except IndexError:
        out.txt_output.set_text(('red bold', u"Geen halte of doorkomsten rond huidig tijdstip gevonden"))
    except TypeError:
        out.txt_output.set_text(('red bold', u"Couldn't reach api. Is there an internet connection?"))


def search_halte(out: Output, query: str) -> None:
    """Search for halte"""
    data = delijnapi.api_search_halte(query)
    if data is None:
        return
    if not data['haltes']:
        out.txt_output.set_text(('red bold', "\nNiets gevonden.probeer een andere zoekterm"))
    else:
        search_output = get_halte_search_results_text(data, query)
        out.set_search_halte_menu(search_output)
        save_query(query)
        global state, last_search
        state = States.search_halte_menu
        last_search = data


class States(Enum):
    main = 0
    doorkomsten_menu = 1
    search_halte_menu = 2
    filter_menu = 3


if __name__ == '__main__':
    signal(SIGINT, signal_handler)
    signal(SIGHUP, signal_handler)
    last_query = get_last_query()
    # todo: what to do with all these globals?
    line_filter = None
    state = States.main
    output = Output()
    last_doorkomsten: dict = {}
    last_search: dict = {}
    loop = urwid.MainLoop(output.original_widget, unhandled_input=unhandled_input_handler, palette=PALETTE)
    loop.run()
    exit(0)
