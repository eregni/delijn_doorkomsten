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

# TODO: parse info about delays/disruptions/detours
# TODO: unicode waiting animation (urwid overlay + progressbar?)
# TODO: Use buttons in the output box
"""
# Postpone evaluation for type annonations https://www.python.org/dev/peps/pep-0563/
from __future__ import annotations

from enum import Enum
from signal import signal, SIGINT, SIGHUP
from typing import Optional

import requests.exceptions
from requests import RequestException, ConnectionError
from urwid import Padding, Divider, Edit, Text, Button, Columns, Pile, Filler, LineBox, MainLoop, ExitMainLoop

import delijn_service
from bookmarks import BOOKMARKS
from tui import PALETTE

QUERY_LOG = "search.txt"
PROGRAM_TITLE = "\U0001F68B \U0001F68C \U0001F68B De lijn doorkomsten \U0001F68C \U0001F68B \U0001F68C"
DOORKOMSTEN_REFRESH = 60


class Output(Padding):
    """
    Packaging of the urwid objects.
    Methods control the appearance of the ui
    """

    def __init__(self, program: Program):
        self.program = program

        self.div = Divider(div_char='-')

        self.input_user = UserInput(Edit(""), program, self)
        self.error_output = Text("")
        self._output_box = Pile([], focus_item=0)
        self.txt_info = Text("")

        self.button_exit = Button("Afsluiten", on_press=exit_urwid)
        self.button_bookmarks = Button("Favorieten", on_press=button_bookmarks_handler, user_data=self)
        self.button_new_search = Button("Home", on_press=button_main_menu_handler, user_data=self)
        self.button_filter = Button("Filteren", on_press=button_filter_handler, user_data=self)
        self.button_remove_filter = Button("Verwijder filter", on_press=button_remove_filter_handler, user_data=self)
        self.buttons = Columns([self.button_exit], dividechars=1, box_columns=[self.button_exit])

        self.pile = Pile([
            self.input_user,
            self.div,
            self._output_box,
            self.div,
            ('pack', self.buttons)
        ], focus_item=0)

        self.main_filler = Filler(self.pile, valign='top')
        self.main_window = LineBox(Padding(self.main_filler, left=1), title=PROGRAM_TITLE)

        super().__init__(self.main_window)
        self.set_main_menu()

    @property
    def output_box(self):
        return self._output_box

    @output_box.setter
    def output_box(self, value: list[Text]):
        self.set_output_box_items(value)

    def _set_buttons(self, buttons: list[Button]):
        new_buttons = [(btn, Columns.options('given', len(btn.label) + 4)) for btn in buttons]
        setattr(self.buttons, 'contents', new_buttons)
        setattr(self.buttons, 'box_buttons', buttons)

    def set_main_menu(self):
        self.input_user.original_widget.set_caption(('bold', "Geef haltenummer of zoekterm: "))
        self.input_user.original_widget.set_edit_text("")
        self.set_output_box_items(get_bookmarks())
        self._set_buttons([
            self.button_bookmarks,
            self.button_exit
        ])

        if self.program.last_query:
            self.txt_info.set_text(f"Druk op enter om terug '{self.program.last_query}' op te zoeken")
            if self.txt_info not in [w[0] for w in self.pile.contents]:
                self.pile.contents.insert(0, (self.txt_info, (Pile.options())))
            self.pile.focus_item = 1

    def set_search_halte_menu(self, search_result: list[Text]):
        keys = [*range(len(search_result))]
        # first item in last_search is a summary line
        self.input_user.original_widget.set_caption(('bold', f"Kies een nr({min(keys) + 1}-{max(keys)}): "))
        self.set_output_box_items(search_result)
        self._set_buttons([
            self.button_new_search,
            self.button_exit
        ])

        self.pile.contents = [w for w in self.pile.contents if w[0] != self.txt_info]
        setattr(self.pile, 'focus_position', 0)

    def set_doorkomsten_menu(self, doorkomsten: list[Text]):
        if self.program.line_filter:
            caption_text = "Druk 'f' om de filter te verwijderen. 'Enter' om te vernieuwen"
        elif len(get_lines_from_doorkomsten(self.program.last_doorkomsten)) == 1:
            caption_text = "Druk op 'Enter' om te vernieuwen"
        else:
            caption_text = "Druk 'f' om te filteren op lijn. 'Enter' om te vernieuwen"

        self.input_user.original_widget.set_caption(caption_text)
        self.set_output_box_items(doorkomsten)

        buttons = [self.button_new_search, self.button_exit]
        lines = get_lines_from_doorkomsten(self.program.last_doorkomsten)
        if len(lines) > 1:
            buttons.insert(1, self.button_filter)
        elif self.program.line_filter:
            buttons.insert(1, self.button_remove_filter)

        self._set_buttons(buttons)
        self.pile.contents = [w for w in self.pile.contents if w[0] != self.txt_info]
        self.pile.focus_position = 0

    def set_choose_line_filter_menu(self, lines: list[str]):
        self.input_user.original_widget.set_caption(f"Kies lijn nummer ({', '.join(lines)}): ")
        self._set_buttons([
            self.button_new_search,
            self.button_exit
        ])
        setattr(self.pile, 'focus_position', 0)

    def set_filtered_doorkomsten_menu(self, doorkomsten: Text):
        self.txt_output.set_text(doorkomsten)
        self._set_buttons([
            self.button_new_search,
            self.button_remove_filter,
            self.button_exit
        ])

    def set_output_box_items(self, items: list[Text]):
        """Replace items with new widget list"""
        new_items = [(item, Pile.options()) for item in items]
        self._output_box.contents = new_items

    def set_error_message(self, message: str, clear=False):
        """
        Display red error message in the output_box
        If clear == True -> Clear the output box as well
        """
        if clear:
            self._output_box.contents.clear()

        urwid_text = (Text(('red bold', message)), Pile.options())
        if not clear and self._output_box.contents[0][0].attrib[0][0] == 'red bold':
            # Overwrite existing error message
            self._output_box.contents[0] = urwid_text
        else:
            self._output_box.contents.insert(0, urwid_text)


def doorkomsten_alarm_handler(_loop: MainLoop, out: Output):
    if output.program.state == States.DOORKOMSTEN_MENU:
        output.input_user.keypress((), 'enter')
    _loop.set_alarm_in(DOORKOMSTEN_REFRESH, doorkomsten_alarm_handler, user_data=out)


def button_bookmarks_handler(button: Button, out: Output) -> None:
    out.set_output_box_items(get_bookmarks())


def button_main_menu_handler(button: Button, out: Output) -> None:
    out.program.state = States.MAIN
    out.program.last_search.clear()
    out.program.last_doorkomsten.clear()
    out.set_main_menu()


def button_filter_handler(button: Button, out: Output) -> None:
    out.program.line_filter = None
    lines = get_lines_from_doorkomsten(out.program.last_doorkomsten)
    out.set_choose_line_filter_menu(lines)


def button_remove_filter_handler(button: Button, out: Output) -> None:
    out.program.line_filter = None
    out.program.doorkomsten(out, out.program.last_doorkomsten['haltenummer'])


def exit_urwid(*args):
    raise ExitMainLoop()


def unhandled_input_handler(key):
    if key in ('q', 'Q'):
        raise ExitMainLoop()


def signal_handler(*args) -> None:
    """Handler for SIGINT signal"""
    exit_urwid("signal")


class Program:
    def __init__(self):
        # todo: encapsulate properties who should be private (states are set all over the program :(
        self.state: States = States.MAIN
        self.last_query: str = get_last_query()
        self.last_doorkomsten: dict = {}
        self.last_search: dict = {}
        self.line_filter: str = ""

    def doorkomsten(self, out: Output, halte_nummer: str, entiteitnummmer: str = None) -> int:
        """
        Process doorkomsten
        Returns 0 on success. 1 on failure
        """
        try:
            halte, doorkomsten = delijn_service.get_doorkomsten(halte_nummer, entiteitnummmer)

            if not doorkomsten['halteDoorkomsten']:
                out.set_error_message("Geen halte of doorkomsten gevonden rond huidig tijdstip")
                return 0

            self.last_doorkomsten = doorkomsten['halteDoorkomsten'][0]
            if self.line_filter:
                self.last_doorkomsten['doorkomsten'] = [item for item in self.last_doorkomsten['doorkomsten'] if
                                                        item['lijnnummer'] == int(self.line_filter)]

            doorkomsten_output = delijn_service.get_doorkomsten_text(halte, self.last_doorkomsten)
            out.set_doorkomsten_menu(doorkomsten_output)
            return 0

        except RequestException as ex:
            fetch_api_exception(out, ex)
            return 1

    def search_halte(self, out: Output, query: str) -> None:
        """Process halte search"""
        try:
            data = delijn_service.search_halte(query)

            if data['aantalHits'] == 0:
                out.set_error_message("Niets gevonden. Probeer een andere zoekterm", clear=True)
                return
            else:
                search_output = delijn_service.get_halte_search_results_text(data, query)

                out.set_search_halte_menu(search_output)
                save_query(query)
                self.last_query = str(query)
                self.state = States.SEARCH_HALTE_MENU
                self.last_search = data

        except RequestException as ex:
            fetch_api_exception(out, ex)
            return

    def process_userinput_main(self, out: Output, input_text: str):
        if input_text == '' and self.last_query:
            input_text = self.last_query

        if input_text.isdigit():
            input_int = int(input_text)
            if input_int - 1 in range(len(BOOKMARKS)):
                bookmark = BOOKMARKS[input_int - 1]
                if self.doorkomsten(out, bookmark.halte_nummer, bookmark.entiteit) == 0:
                    save_query(BOOKMARKS[input_int - 1].halte_nummer)
                    self.last_query = input_text
                self.state = States.DOORKOMSTEN_MENU
            else:
                self.doorkomsten(out, str(input_int))

        else:
            self.search_halte(out, input_text)

    def process_userinput_doorkomsten(self, out: Output, user_input: str):
        if user_input == 'enter':
            self.doorkomsten(out, self.last_query)
        elif user_input == 'f' and self.line_filter:
            self.line_filter = None
            self.doorkomsten(out, self.last_query)
        elif user_input == 'f':
            lines = get_lines_from_doorkomsten(self.last_doorkomsten)
            if len(lines) < 2:
                return

            out.set_choose_line_filter_menu(lines)
            self.state = States.FILTER_MENU

    def process_userinput_search_halte(self, out: Output, input_text: str):
        if input_text.isdigit() and int(input_text) - 1 in range(len(self.last_search['haltes'])):
            halte_nr = self.last_search['haltes'][int(input_text) - 1]['haltenummer']
            enititeit_nr = self.last_search['haltes'][int(input_text) - 1]['entiteitnummer']
            self.doorkomsten(out, halte_nr, enititeit_nr)
        else:
            out.set_error_message(f"Ongeldige invoer: \"{input_text}\"")

    def process_userinput_filter(self, out: Output, input_text: str):
        if input_text in get_lines_from_doorkomsten(self.last_doorkomsten):
            self.line_filter = input_text
            self.doorkomsten(out, self.last_doorkomsten['haltenummer'])
        else:
            out.set_error_message(f"Ongeldige invoer: \"{input_text}\"")


class UserInput(Padding):
    """Handle user text input"""

    def __init__(self, user_input: Edit, program: Program, out: Output):
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


def get_bookmarks() -> list[Text]:
    """Give list with Text items from bookmark list"""
    bookmark_length = max([len(halte.bookmark_name) for halte in BOOKMARKS])
    urwid_text_list = [Text(('lightcyan bold', "Favorieten"))]
    for index, halte in enumerate(BOOKMARKS):
        index_text = f"{index + 1})"
        bookmark_text = f" {index_text:<4}{halte.bookmark_name:<{bookmark_length}} ({halte.halte_nummer})"
        # add in a tuple
        # -> /home/edoardo/PycharmProjects/delijn_doorkomsten/venv/lib/python3.10/site-packages/urwid/container.py
        urwid_text = Text(('lightcyan', bookmark_text))
        urwid_text_list.append(urwid_text)

    return urwid_text_list


def get_lines_from_doorkomsten(doorkomsten: dict) -> list[str]:
    """Give a list containing the line nrs from the doorkomsten data returned by delijn api"""
    lines = [line['lijnnummer'] for line in doorkomsten['doorkomsten']]
    lines = list(dict.fromkeys(lines))
    lines.sort()
    return list(map(str, lines))


def fetch_api_exception(out: Output, ex: RequestException):
    """Handler for exceptions raised by requests"""
    if isinstance(ex, ConnectionError):
        out.set_error_message("Cannot reach delijn api. Is there an internet connection?", clear=True)
    # last 'catch-all'
    elif isinstance(ex, RequestException):
        out.set_error_message(f"{ex}", clear=True)
    else:
        # raise unhandled exception
        raise ex


class States(Enum):
    MAIN = 0
    DOORKOMSTEN_MENU = 1
    SEARCH_HALTE_MENU = 2
    FILTER_MENU = 3


signal(SIGINT, signal_handler)
signal(SIGHUP, signal_handler)

prog = Program()
output = Output(prog)
loop = MainLoop(output.original_widget, unhandled_input=unhandled_input_handler, palette=PALETTE)
loop.set_alarm_in(DOORKOMSTEN_REFRESH, doorkomsten_alarm_handler, user_data=output)
loop.run()
