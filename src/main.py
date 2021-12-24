#!/usr/bin/env python3
"""
Terminal program to show realtime info from De lijn. I wrote this thing because the official
(android) app works awfully slow on my phone. A solution is to make a terminal program with
(a lot) fewer features:

*   search realtime info for a specific bus stop. When there's no result search for
    a stop by name

*   Filter search results by line nr

I've used Dutch words in the code and comments because I kept the same variable names as found in
the api from De Lijn

used sources:
API https://delijn.docs.apiary.io/

I used the old api because the new one (https://data.delijn.be/) needs much more api calls and code.
"""
from signal import signal, SIGINT, SIGHUP
from datetime import datetime, timedelta
from typing import Union

import urwid

import delijnapi
from tui import PALETTE, ICON
import bookmarks

QUERY_LOG = "search.txt"
FAVORITES = [item for item in bookmarks.BOOKMARKS.items()]
PROGRAM_TITLE = "\U0001F68B \U0001F68C \U0001F68B De lijn doorkomsten \U0001F68C \U0001F68B \U0001F68C"


class Output(urwid.Padding):
    """
    Packaging of the urwid objects.
    Methods control the appearance of the ui
    """
    def __init__(self):
        self.div = urwid.Divider(div_char='-')

        edit = urwid.Edit("")
        self.input_user = UserInput(edit)

        self.txt_output = urwid.Text(u"TEEEEEEST", align='left')  # TODO change to listbox
        self.txt_info = urwid.Text(u"")

        self.button_exit = urwid.Button(u"Afsluiten", on_press=exit_urwid)
        self.button_bookmarks = urwid.Button(u"Favorieten", on_press=button_bookmarks_handler, user_data=self.txt_output)
        self.button_new_search = urwid.Button(u"Nieuwe zoekopdracht", on_press=button_main_menu_handler)
        self.buttons = urwid.Columns([], dividechars=1, focus_column=0)  # todo use property?
        # todo add button <remove/filter> and <new search> in submenus

        self.pile = urwid.Pile([self.txt_output])  # todo use property?

        main_filler = urwid.Filler(self.pile, valign='top')
        self.main_window = urwid.LineBox(urwid.Padding(main_filler, left=1), title=PROGRAM_TITLE)

        super().__init__(self.main_window)
        self.set_main_menu()

    def _set_buttons(self, buttons: list[urwid.Button]):
        self.buttons = urwid.Columns(
            widget_list=[(len(btn.label) + 4, self.button_exit) for btn in buttons],
            dividechars=1,
            box_columns=buttons
        )

    def _set_pile(self, items: list[Union[urwid.Widget, tuple[str, urwid.Widget]]], focus_item: int):
        self.pile = urwid.Pile(items, focus_item=focus_item)

    def set_main_menu(self):
        self.input_user.original_widget.set_caption(('bold', "Geef haltenummer of zoekterm"))
        self.input_user.original_widget.set_edit_text("")
        self.txt_output.set_text(get_bookmarks())
        self._set_buttons([self.button_exit])
        self._set_pile([
            self.input_user,
            self.div,
            self.txt_output,
            self.div,
            ('pack', self.buttons)
        ], focus_item=0)

        if last_query:
            self.txt_info.set_text(f"Druk op enter om terug '{last_query}' op te zoeken")
            self.pile.widget_list.insert(0, self.txt_info)
            self.pile.focus_item = 1

    def set_search_halte(self):
        raise NotImplementedError

    def set_doorkomsten(self):
        raise NotImplementedError

    def set_filtered_doorkomsten(self):
        raise NotImplementedError


class UserInput(urwid.Padding):
    """Handle user text input"""
    def __init__(self, user_input: urwid.Edit):
        super().__init__(user_input)

    def keypress(self, size, key):
        if key != 'enter':
            return super(UserInput, self).keypress(size, key)

        edit_text: str = self.original_widget.edit_text
        if edit_text == '' and output.last_query:
            edit_text = last_query

        if edit_text.isdigit():
            nr = int(edit_text)
            if nr - 1 in range(len(bookmarks.BOOKMARKS)):
                # todo update doorkomsten()
                doorkomsten(FAVORITES[nr - 1][1], output)
            else:
                pass  # todo update doorkomsten()
                doorkomsten(nr, output)
        else:
            search_halte(edit_text, output)

        return super(UserInput, self).original_widget.set_edit_text("")


def save_query(query_input: [str, int]) -> None:
    """Put search query in a text file"""
    with open(QUERY_LOG, "w") as file:
        file.write(str(query_input))


def get_last_query() -> str:
    """Read last search entry from text file"""
    try:
        with open(QUERY_LOG, "r") as file:
            return file.readline().rstrip()
    except FileNotFoundError:
        return ""


def print_doorkomsten(lijnen: dict,  output_text: urwid.Text) -> None:
    """print parsed data in terminal"""
    text_color = Colors.Fg.lightblue
    print(f"\n{text_color}{lijnen['omschrijvingLang']} - haltenr: {lijnen['halteNummer']}")
    text_color = Colors.Fg.lightgreen

    for item in lijnen['lijnen']:
        vertrektijd = datetime.fromtimestamp(item['vertrekTheoretischeTijdstip'] / 1000)
        vertrektijd_text = ""
        delay_text = ""

        if "CANCELLED" in item['predictionStatussen']:
            realtime_text = "Rijdt niet"
        elif "DELETED" in item['predictionStatussen']:
            realtime_text = "Rijdt niet"
        elif "REALTIME" in item['predictionStatussen']:
            realtime_text = item['vertrekTijd']
            try:
                vertrektijd_rt = datetime.fromtimestamp(item['vertrekRealtimeTijdstip'] / 1000)
                vertrektijd_text = vertrektijd.strftime('%H:%M')
                if vertrektijd_rt > vertrektijd + timedelta(seconds=60):
                    delay = vertrektijd_rt - vertrektijd
                    delay_text = f"{Colors.Fg.red}+{delay.seconds // 60}\'{text_color}"
                elif vertrektijd_rt < vertrektijd - timedelta(seconds=60):
                    delay = vertrektijd - vertrektijd_rt
                    # add an extra min to increase chances of catching your bus...
                    delay_text = f"{Colors.Fg.red}-{(delay.seconds // 60) + 1}\'{text_color}"
            except TypeError:  # 'vertrekRealtimeTijdstip' = None (Sometimes, the api doesn't return the calculated ETA)
                pass
        else:
            realtime_text = "GN RT"

        icon = ICON.get(item['lijnType'], "")
        print(f"{text_color}{icon} {item['lijnType']:<5}{ item['lijnNummerPubliek']:<4}{item['bestemming']:<25}"
              f"{realtime_text:<7}{vertrektijd_text:<7}{delay_text}")
        text_color = Colors.Fg.yellow if text_color == Colors.Fg.lightgreen else Colors.Fg.lightgreen

    print(Colors.reset)


def print_halte_search_results(table: dict, query: str, output_text: urwid.Text) -> None:
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

    output_text.set_text(text)


def get_bookmarks() -> list[tuple[str, str]]:
    """Give string + urwid markup from bookmark list"""
    stop_length = max([len(stop) for stop, _ in FAVORITES])
    bookmark_text = ""
    for index, (stop, nr) in enumerate(FAVORITES):
        index_text = f"{index + 1})"
        bookmark_text += f" {index_text:<4}{stop:<{stop_length}} ({nr})\n"

    return [('lightcyan bold', "Favorieten\n"), ('lightcyan', bookmark_text)]


def doorkomsten(halte_nummer: int, output_text: urwid.Text) -> None:
    """Loop for the doorkomsten table"""
    line_filter = None
    while True:
        try:
            data = delijnapi.api_get_doorkomsten(halte_nummer)
            lijnen = data['halte'][0]
            if line_filter is not None:
                lijnen['lijnen'] = [item for item in lijnen['lijnen'] if item['lijnNummerPubliek'] == line_filter]
            print_doorkomsten(lijnen)
            save_query(halte_nummer)

        except IndexError as e:
            # todo more nuance in exceptions... test!
            output_text.set_text(('red bold', u"Geen doorkomsten gevonden"))
        except TypeError as e:
            output_text.set_text(('red bold', u"Geen doorkomsten gevonden rond huidig tijdstip :-("))
            break
        # todo continue here
        return

        user_input = input("Willekeurige knop = vernieuwen. 0 = opnieuw beginnen, f = filter op lijnnr: ")
        if user_input == '0':
            break
        elif user_input == 'f':
            line_nrs = {line['lijnNummerPubliek'] for line in lijnen['lijnen']}
            lines = ", ".join(line_nrs)
            user_input = input(f"Kies lijnnr ({lines}): ")
            if user_input in line_nrs:
                line_filter = user_input


def search_halte(query: str, out: Output) -> None:
    data = delijnapi.api_search_halte(query)
    if data is None:
        return
    if not data['haltes']:
        out.txt_output.set_text(('red bold', "\nNiets gevonden.probeer een andere zoekterm"))
    else:
        print_halte_search_results(data, query, txt_output)
        save_query(query)
        out.input_user.set_caption(('bold', "Geef nummer: "))
        test = out.pile.focus_position  # todo debug
        # todo set focus on user_input
        return
        # todo continue here: change all button inputs/callbacks. Add buttons...
        user_input = input("\nKies nr. 0 = opnieuw beginnen: ")
        if user_input != '0' and user_input.isdigit():
            user_input = int(user_input) - 1
            haltenr = data['haltes'][user_input]['halteNummer']
            doorkomsten(haltenr, output_text)
        else:
            output_text.set_text(('red bold', "Ongeldige invoer"))


def button_bookmarks_handler(button: urwid.Button, out: Output) -> None:
    out.txt_info.set_text(get_bookmarks())


def button_main_menu_handler(button: urwid.Button, out: Output):
    out.set_main_menu()


def exit_urwid(*args):
    raise urwid.ExitMainLoop()


def unhandled_input_handler(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def signal_handler(*args) -> None:
    """Handler for SIGINT signal"""
    exit_urwid("signal")


if __name__ == '__main__':
    """
        Script flow:
            * Start:
                User input: haltenummer -> Doorkomsten | search by name -> Search halte | bookmark nr -> Doorkomsten
                Buttons: bookmarks, exit
                Output: bookmarks list

                * Search halte:
                    User input: nr search result -> Doorkomsten
                    Buttons: new search -> Start, exit
                    Output: search results

                * Doorkomsten
                    User input: 'f' -> Doorkomsten(filter)
                    Buttons: new search -> Start, refresh, filter, [remove filter], exit
                    Output: doormkomsten [filtered line] (autorefresh each 30 seconds)
        """
    signal(SIGINT, signal_handler)
    signal(SIGHUP, signal_handler)
    last_query = get_last_query()
    output = Output()
    loop = urwid.MainLoop(output.original_widget, unhandled_input=unhandled_input_handler, palette=PALETTE)
    loop.run()
    exit(0)
