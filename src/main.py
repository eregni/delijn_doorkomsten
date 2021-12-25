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
"""
from enum import Enum
from signal import signal, SIGINT, SIGHUP
from datetime import datetime, timedelta

import urwid

import delijnapi
from tui import PALETTE, ICON
import bookmarks

QUERY_LOG = "search.txt"
FAVORITES = [item for item in bookmarks.BOOKMARKS.items()]
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

        self.button_exit = urwid.Button(u"Afsluiten", on_press=exit_urwid)
        self.button_bookmarks = urwid.Button(u"Favorieten", on_press=button_bookmarks_handler, user_data=self)
        self.button_new_search = urwid.Button(u"Nieuwe zoekopdracht", on_press=button_main_menu_handler, user_data=self)
        self.button_filter = urwid.Button(u"Filteren", on_press=button_filter_handler, user_data=line_filter)
        self.button_remove_filter = urwid.Button(u"Filter verwijderen", on_press=button_filter_handler)
        self.buttons = urwid.Columns([], dividechars=1)

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
            self.button_exit,
            self.button_bookmarks
        ])

        global last_query
        if last_query:
            self.txt_info.set_text(f"Druk op enter om terug '{last_query}' op te zoeken")
            if self.txt_info not in [w[0] for w in self.pile.contents]:
                self.pile.widget_list.insert(0, self.txt_info)
            self.pile.focus_item = 1

    def set_search_halte_menu(self, search_result: UrwidText):
        self.input_user.original_widget.set_caption("Kies een nr: ")
        self.txt_output.set_text(search_result)
        self._set_buttons([
            self.button_new_search,
            self.button_exit
        ])

        self.pile.contents = [w for w in self.pile.contents if w[0] != self.txt_info]
        setattr(self.pile, 'focus_position', 0)

    def set_doorkomsten_menu(self, dk: UrwidText):
        self.input_user.original_widget.set_caption("Druk 'f' om te filteren op lijn. 'Enter' om te vernieuwen")
        self.txt_output.set_text(dk)
        self._set_buttons([
            self.button_new_search,
            self.button_filter,
            self.button_exit
        ])

        self.pile.contents = [w for w in self.pile.contents if w[0] != self.txt_info]
        setattr(self.pile, 'focus_position', 0)

    def set_choose_line_filter(self):
        raise NotImplementedError

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
    global state
    global last_doorkomsten
    state = States.main
    last_doorkomsten.clear()
    out.set_main_menu()


def button_filter_handler(button: urwid.Button, out: Output) -> None:
    output.set_choose_line_filter()


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

    def keypress(self, size: tuple, key: str):
        global state
        if state == States.main:
            self._proces_main(size, key)
        elif state == States.doorkomsten_menu:
            self._proces_doorkomsten(size, key)
        elif state == States.search_halte_menu:
            self._process_search_halte(size, key)
        elif state == States.filter_menu:
            self._process_filter(size, key)

    def _proces_main(self, size: tuple, key: str):
        if key != 'enter':
            return super(UserInput, self).keypress(size, key)

        edit_text: str = self.original_widget.edit_text
        global last_query
        if edit_text == '' and last_query:
            edit_text = last_query

        if edit_text.isdigit():
            nr = int(edit_text)
            if nr - 1 in range(len(bookmarks.BOOKMARKS)):
                doorkomsten(output, FAVORITES[nr - 1][1])
            else:
                doorkomsten(output, nr)

        else:
            search_halte(output, edit_text)

        return super(UserInput, self).original_widget.set_edit_text("")

    def _process_doorkomsten(self, size: tuple, key: str):
        raise NotImplementedError

    def _process_search_halte(self, size: tuple, key: str):
        raise NotImplementedError

    def _process_filter(self, size: tuple, key: str):
        raise NotImplementedError


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

        icon = ICON.get(item['lijnType'], "")
        line = [(text_color,
                 f"{icon} {item['lijnType']:<5}{item['lijnNummerPubliek']:<4}{item['bestemming']:<25}{realtime_text:<7}"
                 f"{vertrektijd_text:<7}"),
                '\n' if delay_text is None else delay_text]

        text.extend(line)
        text_color = 'yellow' if text_color == 'green' else 'green'

    return text


def get_halte_search_results_text(table: dict, query: str) -> UrwidText:
    """print parsed data in terminal from 'api_search_halte' function"""
    text = [('lightcyan', f"\n\"{query}\": {len(table)} resultaten\n")]
    text_color = 'green'
    haltes = table['haltes']
    for index, halte in enumerate(haltes):
        lijn_nummers = ", ".join([lijn['lijnNummerPubliek'] for lijn in halte['lijnen']])
        bestemmingen = ", ".join(halte['bestemmingen'])
        text.append((text_color, f"{index + 1}) {halte['omschrijvingLang']} - haltenr: "f"{halte['halteNummer']} - "
                                 f"Lijnen: {lijn_nummers} Richting: {bestemmingen}\n"))
        text_color = 'yellow' if text_color == 'green' else 'green'

    return text


def get_bookmarks() -> UrwidText:
    """Give string + urwid markup from bookmark list"""
    stop_length = max([len(stop) for stop, _ in FAVORITES])
    bookmark_text = ""
    for index, (stop, nr) in enumerate(FAVORITES):
        index_text = f"{index + 1})"
        bookmark_text += f" {index_text:<4}{stop:<{stop_length}} ({nr})\n"

    return [('lightcyan bold', "Favorieten\n"), ('lightcyan', bookmark_text)]


def doorkomsten(out: Output, halte_nummer: int, linefilter: int = None, ) -> None:
    """Process the doorkomsten table"""
    global last_doorkomsten
    try:
        data = delijnapi.api_get_doorkomsten(halte_nummer)
        last_doorkomsten = data['halte'][0]
        if linefilter is not None:
            last_doorkomsten['lijnen'] = [item for item in last_doorkomsten['lijnen'] if item['lijnNummerPubliek'] == linefilter]
        doorkomsten_output = get_doorkomsten_text(last_doorkomsten)
        out.set_doorkomsten_menu(doorkomsten_output)
        save_query(halte_nummer)

    except IndexError as e:
        # todo more nuance in exceptions... test!
        out.txt_output.set_text(('red bold', u"Geen doorkomsten gevonden"))
    except TypeError as e:
        out.txt_output.set_text(('red bold', u"Geen doorkomsten gevonden rond huidig tijdstip :-("))


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
        global state
        state = States.search_halte_menu
        return
        # todo continue here -> implement choose result nr...
        user_input = input("\nKies nr. 0 = opnieuw beginnen: ")
        if user_input != '0' and user_input.isdigit():
            user_input = int(user_input) - 1
            haltenr = data['haltes'][user_input]['halteNummer']
            doorkomsten(haltenr, output_text)
        else:
            output_text.set_text(('red bold', "Ongeldige invoer"))


class States(Enum):
    main = 0
    doorkomsten_menu = 1
    search_halte_menu = 2
    filter_menu = 3


if __name__ == '__main__':
    signal(SIGINT, signal_handler)
    signal(SIGHUP, signal_handler)
    last_query = get_last_query()
    line_filter = None
    state = States.main
    output = Output()
    last_doorkomsten = []
    loop = urwid.MainLoop(output.original_widget, unhandled_input=unhandled_input_handler, palette=PALETTE)
    loop.run()
    exit(0)
