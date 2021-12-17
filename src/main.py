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
import sys
from signal import signal, SIGINT
from datetime import datetime, timedelta

import delijnapi
from tui import Colors, ICON
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


def print_favorites() -> None:
    """Print favorites list"""
    print(Colors.Fg.lightcyan)
    stop_length = max([len(stop) for stop, _ in FAVORITES])
    for index, (stop, nr) in enumerate(FAVORITES):
        index_text = f"{index + 1})"
        print(f"{index_text:<4}{stop:<{stop_length}} ({nr})")
    print(Colors.reset)


def doorkomsten(halte_nummer: int):
    """Loop for the doorkomsten table"""
    line_filter = None
    while True:
        try:
            data = delijnapi.api_get_doorkomsten(halte_nummer)
            lijnen = data['halte'][0]
            if line_filter is not None:
                filtered = filter_doorkomsten(line_filter, lijnen)
                print_doorkomsten(filtered)
            else:
                print_doorkomsten(lijnen)

            save_query(halte_nummer)

        except (IndexError, TypeError) as e:
            print("Geen doorkomsten gevonden rond huidig tijdstip :-(")
            break

        user_input = input("Willekeurige knop = vernieuwen. 0 = opnieuw beginnen, f = filter op lijnnr: ")
        if user_input == '0':
            break
        elif user_input == 'f':
            line_nrs = {line['lijnNummerPubliek'] for line in lijnen['lijnen']}
            lines = ", ".join(line_nrs)
            user_input = input(f"Kies lijnnr ({lines}): ")
            if user_input in line_nrs:
                line_filter = user_input


def filter_doorkomsten(line_filter: str, lijnen: dict) -> dict:
    """filter by a line-nr"""
    lijnen['lijnen'] = [item for item in lijnen['lijnen'] if item['lijnNummerPubliek'] == line_filter]
    return lijnen


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


def main():
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
    print("######################################")
    print("\U0001F68B \U0001F68C \U0001F68B De lijn doorkomsten \U0001F68C \U0001F68B \U0001F68C")
    print("######################################")
    print_favorites()
    while True:
        if last_query:
            print(f"Druk enter om terug '{last_query}' op te zoeken")

        user_input = input("Halte (nr of naam), f = favorieten, 0 = afsluiten: ") or last_query

        if user_input == '0':
            break

        if user_input == '':  # user pressed [enter] and last_query is None
            continue

        if user_input == 'f':
            print_favorites()

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input - 1 in range(len(FAVORITES)):
                doorkomsten(FAVORITES[user_input - 1][1])
            else:
                doorkomsten(user_input)

        else:
            search_halte(user_input)


if __name__ == '__main__':
    signal(SIGINT, sigint_handler)
    main()
