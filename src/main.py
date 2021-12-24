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
import urwid

import delijnapi
from tui import PALETTE, ICON
import bookmarks

QUERY_LOG = "search.txt"
FAVORITES = [item for item in bookmarks.BOOKMARKS.items()]


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


def print_doorkomsten(lijnen: dict) -> None:
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
    output_text.set_text(('lightcyan', f"\n\"{query}\""))
    text_color = 'green'
    haltes = table['haltes']
    text = []
    for index, halte in enumerate(haltes):
        lijn_nummers = ", ".join([lijn['lijnNummerPubliek'] for lijn in halte['lijnen']])
        bestemmingen = ", ".join(halte['bestemmingen'])
        text.append((text_color, f"{index + 1}) {halte['omschrijvingLang']} - haltenr: "f"{halte['halteNummer']} - "
                                 f"Lijnen: {lijn_nummers} Richting: {bestemmingen}\n"))
        text_color = 'yellow' if text_color == 'green' else 'green'

    output_text.set_text(text)


def print_bookmarks(output_text: urwid.Text) -> None:
    """Print bookmark list"""
    stop_length = max([len(stop) for stop, _ in FAVORITES])
    bookmark_text = ""
    for index, (stop, nr) in enumerate(FAVORITES):
        index_text = f"{index + 1})"
        bookmark_text += f" {index_text:<4}{stop:<{stop_length}} ({nr})\n"

    output_text.set_text([('lightcyan bold', "Favorieten\n"), ('lightcyan', bookmark_text)])


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


def search_halte(query: str, output_text: urwid.Text, user_input: urwid.Edit) -> None:
    data = delijnapi.api_search_halte(query)
    if data is None:
        return
    if not data['haltes']:
        output_text.set_text(('red bold', "\nNiets gevonden.probeer een andere zoekterm"))
    else:
        print_halte_search_results(data, query, txt_output)
        save_query(query)
        user_input.set_caption(('bold', "Geef nummer: "))
        return
        # todo continue here: change all button inputs/callbacks. Add buttons...
        user_input = input("\nKies nr. 0 = opnieuw beginnen: ")
        if user_input != '0' and user_input.isdigit():
            user_input = int(user_input) - 1
            haltenr = data['haltes'][user_input]['halteNummer']
            doorkomsten(haltenr, output_text)
        else:
            output_text.set_text(('red bold', "Ongeldige invoer"))


def button_bookmarks_handler(button: urwid.Button, text: urwid.Text) -> None:
    print_bookmarks(text)


def exit_urwid(*args):
    raise urwid.ExitMainLoop()


def unhandled_input_handler(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def signal_handler(*args) -> None:
    """Handler for SIGINT signal"""
    exit_urwid("signal")


class UserInput(urwid.Padding):
    def keypress(self, size, key):
        if key == 'enter':
            edit_text: str = self.original_widget.edit_text
            if edit_text == '' and last_query:
                edit_text = last_query

            if edit_text.isdigit():
                nr = int(edit_text)
                if nr - 1 in range(len(bookmarks.BOOKMARKS)):
                    # todo update doorkomsten()
                    doorkomsten(FAVORITES[nr - 1], txt_output)
                else:
                    pass  # todo update doorkomsten()
                    doorkomsten(nr, txt_output)
            else:
                search_halte(edit_text, txt_output, input_user.original_widget)

            return super(UserInput, self).original_widget.set_edit_text("")

        else:
            return super(UserInput, self).keypress(size, key)


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

    # urwid layout + callbacks
    program_title = "\U0001F68B \U0001F68C \U0001F68B De lijn doorkomsten \U0001F68C \U0001F68B \U0001F68C"
    div = urwid.Divider(div_char='-')
    edit = urwid.Edit(('bold', u"Geef haltenummer of zoekterm: "))
    txt_output = urwid.Text(u"", align='left')  # TODO FIRST turn into scrollList before continuing adjusting functions
    txt_info = urwid.Text(u"")
    input_user = UserInput(edit)
    # urwid.connect_signal(input_user, 'change', input_handler, user_args=[txt_info, txt_output])
    button_exit = urwid.Button(u"Afsluiten", on_press=exit_urwid)
    button_bookmarks = urwid.Button(u"Favorieten", on_press=button_bookmarks_handler, user_data=txt_output)
    # todo add button <remove/filter> and <new search> in submenus
    button_column = urwid.Columns([
        # width -> len(Button.label + 4 button chars. 'pack' didn't work very well...
        (len(button_exit.label) + 4, button_exit),t
        (len(button_bookmarks.label) + 4, button_bookmarks)
    ], dividechars=1, box_columns=[
        button_exit,
        button_bookmarks
    ])

    pile = urwid.Pile([
        input_user,
        div,
        txt_output,
        div,
        ('pack', button_column)
    ], focus_item=1)

    main_window = urwid.Filler(pile, valign='top')
    main_window = urwid.LineBox(urwid.Padding(main_window, left=1), title=program_title)
    loop = urwid.MainLoop(main_window, unhandled_input=unhandled_input_handler, palette=PALETTE)

    # program
    last_query = get_last_query()
    if last_query:
        txt_info.set_text(f"Druk op enter om terug '{last_query}' op te zoeken")
        pile.widget_list.insert(0, txt_info)
        pile.focus_item = 1

    print_bookmarks(txt_output)

    loop.run()
    exit(0)
