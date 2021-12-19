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

todo: indications for no internet/api connection???
Todo: correct type hints for cursesWindow
"""
import sys
import curses
import curses.ascii
from signal import signal, SIGINT
from datetime import datetime, timedelta

import delijnapi
from tui import ICON
from favorites import FAVORITES

QUERY_LOG = "search.txt"


def sigint_handler(sig, frame) -> None:
    """Handler for SIGINT signal"""
    print("\nctrl-c. Bye!")
    sys.exit(0)


def save_query(query_input: [str, int]) -> None:
    """Put search query in a text file"""
    with open(QUERY_LOG, "w") as file:
        file.write(str(query_input))


def get_last_query() -> str:
    """Read last search entry from text file"""
    try:
        with open(QUERY_LOG, "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""


def print_doorkomsten(lijnen: dict, output_window: curses.window) -> None:
    """print parsed data in terminal"""
    output_window.clear()
    text_color = curses.color_pair(1)
    output_window.addstr(0, 1, f"{lijnen['omschrijvingLang']} - haltenr: {lijnen['halteNummer']}", text_color)
    text_color = curses.color_pair(2)

    for index, item in enumerate(lijnen['lijnen']):
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
                    delay_text = f"+{delay.seconds // 60}\'"
                elif vertrektijd_rt < vertrektijd - timedelta(seconds=60):
                    delay = vertrektijd - vertrektijd_rt
                    # add an extra min to increase chances of catching your bus...
                    delay_text = f"-{(delay.seconds // 60) + 1}\'"
            except TypeError:  # 'vertrekRealtimeTijdstip' = None (Sometimes, the api doesn't return the calculated ETA)
                pass
        else:
            realtime_text = "GN RT"

        icon = ICON.get(item['lijnType'], "")
        output_window.addstr(index + 1, 2,
                             f"{icon} {item['lijnType']:<5}{ item['lijnNummerPubliek']:<4}{item['bestemming']:<25}"
                             f"{realtime_text:<7}{vertrektijd_text:<7}{delay_text}", text_color)

        text_color = curses.color_pair(3) if text_color == curses.color_pair(2) else curses.color_pair(2)

    output_window.refresh()


def print_halte_search_results(table: dict, query: str) -> None:
    """print parsed data in terminal from 'api_search_halte' function"""
    text_color = Colors.Fg.lightblue
    print(f"\n{text_color}\"{query}\"")
    text_color = Colors.Fg.lightgreen
    haltes = table['haltes']
    for index, halte in enumerate(haltes):
        lijn_nummers = ", ".join([lijn['lijnNummerPubliek'] for lijn in halte['lijnen']])
        bestemmingen = ", ".join(halte['bestemmingen'])
        print(f"{text_color}{index + 1}) {halte['omschrijvingLang']} - haltenr: {halte['halteNummer']} - Lijnen: "
              f"{lijn_nummers} Richting: {bestemmingen}")

        text_color = Colors.Fg.yellow if text_color == Colors.Fg.lightgreen else Colors.Fg.lightgreen

    print(Colors.reset)


def print_favorites(window) -> None:
    """Print favorites list"""
    stop_length = max([len(stop) for stop, _ in FAVORITES])
    window.clear()
    window.resize(len(FAVORITES) + 1, window.getmaxyx()[1])
    window.addstr(0, 1, "Favorieten:", curses.A_BOLD)
    for index, (stop, nr) in enumerate(FAVORITES):
        index_text = str(index + 1) + ')'
        window.addstr(index + 1, 2, f"{index_text:<4}{stop:<{stop_length}} ({nr})", curses.color_pair(1))

    window.refresh()


def doorkomsten(halte_nummer: int, output_window: curses.window, keys_window: curses.window, input_window: curses.window):
    """Loop for the doorkomsten table"""
    line_filter = None
    while True:
        try:
            # todo: inform user when halte nr does not exists
            data = delijnapi.api_get_doorkomsten(halte_nummer)
            lijnen = data['halte'][0]
            if line_filter is not None:
                lijnen['lijnen'] = [item for item in lijnen['lijnen'] if item['lijnNummerPubliek'] == line_filter]

            print_doorkomsten(lijnen, output_window)
            save_query(halte_nummer)

        except (IndexError, TypeError) as e:
            output_window.clear()
            output_window.addstr(0, 1, "Geen doorkomsten gevonden rond huidig tijdstip :-(", curses.color_pair(1))
            output_window.refresh()
            break

        keys_window.clear()
        keys_window.addstr(0, 1, "Willekeurige knop = vernieuwen. 0 = opnieuw beginnen, f = filter op lijnnr")
        keys_window.refresh()
        keys_window.getch()
        #user_input = input("Willekeurige knop = vernieuwen. 0 = opnieuw beginnen, f = filter op lijnnr: ")
        # todo continue here
        if user_input == '0':
            break
        elif user_input == 'f':
            line_nrs = {line['lijnNummerPubliek'] for line in lijnen['lijnen']}
            lines = ", ".join(line_nrs)
            user_input = input(f"Kies lijnnr ({lines}): ")
            if user_input in line_nrs:
                line_filter = user_input


def search_halte(query: str) -> None:
    data = delijnapi.api_search_halte(query)
    if data is None:
        return
    if not data['haltes']:
        print("\nNiets gevonden.probeer een andere zoekterm")
    else:
        print_halte_search_results(data, query)
        save_query(query)
        user_input = input("\nKies nr. 0 = opnieuw beginnen: ")
        if user_input != '0' and user_input.isdigit():
            user_input = int(user_input) - 1
            haltenr = data['haltes'][user_input]['halteNummer']
            doorkomsten(haltenr)
        else:
            print("Ongeldige invoer")


def clear_input_window(window: curses.window):
    window.clear()
    window.addstr(0, 1, "invoer: ", curses.A_BOLD)
    window.refresh()


def main(stdscr: curses.window):
    """
    Script:
    1) Ask user input
    2) User input is
        int/haltenr -> get doorkomst info or select favorite
        string      -> Search halte by name
        'f'         -> list favorite stops
        '0'         -> exit script
    """
    last_query = get_last_query()

    curses.curs_set(0)
    curses.echo()
    curses.nocbreak()

    # Color setup
    curses.init_color(curses.COLOR_CYAN, 321, 965, 965)  # -> light cyan
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    max_height, max_width = stdscr.getmaxyx()
    stdscr.clear()

    win_output = curses.newwin(max_height - 5, max_width - 2, 2, 1)
    win_keys = curses.newwin(2, max_width - 2, max_height - 5, 1)
    win_input = curses.newwin(2, max_width - 2, max_height - 3, 1)

    stdscr.box()
    stdscr.addstr(0, 4, f" \U0001F68B \U0001F68C \U0001F68B De lijn doorkomsten \U0001F68C \U0001F68B \U0001F68C ")
    stdscr.refresh()
    print_favorites(win_output)

    if last_query:
        win_keys.addstr(0, 1, f"Druk op enter om terug '{last_query}' op te zoeken")
    win_keys.addstr(1, 1, "Geef haltenummer/zoekterm/favoriet, f = favorieten, 0 = afsluiten")
    win_keys.refresh()

    clear_input_window(win_input)

    while True:
        user_input = win_input.getstr(0, 9, 30)
        clear_input_window(win_input)
        if user_input == '0':
            break

        if user_input == b'':  # user pressed [enter] and last_query is None
            continue

        if user_input == b'f':
            print_favorites(win_output)

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input - 1 in range(len(FAVORITES)):
                doorkomsten(FAVORITES[user_input - 1][1], win_output, win_keys, win_input)
            else:
                doorkomsten(user_input, win_output, win_keys, win_input)

        else:
            search_halte(user_input, win_output)


if __name__ == '__main__':
    signal(SIGINT, sigint_handler)
    curses.wrapper(main)
