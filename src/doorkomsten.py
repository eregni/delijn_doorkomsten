#!/usr/bin/env python3
"""
Program to show realtime info from De lijn. I wrote this thing because the official
(android) app works awefully slow on my phone. A solution is to make a terminal program with less
possibilities:

*   search realtime for a specific bus/tram stop by it's haltenr. When there's no result search for
    a stop by name

I've used dutch words in the code and comments because I kept the same variable names as found in
the api from De Lijn

usefull sources:
API https://delijn.docs.apiary.io/
(useless api ;) ) https://data.delijn.be
todo: storing op lijn melden
todo: add colors/more layout fancyness
todo: leave on github
"""
import time
import os
import sys
from typing import Union
from signal import signal, SIGINT
import requests

QUERY_LOG = "search.txt"
API_CORE = 'https://www.delijn.be/rise-api-core/haltes/vertrekken'
API_SEARCH = 'https://www.delijn.be/rise-api-search'
ICON = {
    'bus': '\U0001F68C',
    'tram': '\U0001F68B',
    'metro': '\U0001F687',
}


def sigint_handler(sig, frame) -> None:
    """Handler for SIGINT signal"""
    print("\nctrl-c. Bye!")
    sys.exit(0)


def api_get_doorkomsten(halte: Union[str, int]) -> dict:
    """Api call. Get realtime info from halte"""
    entiteit = halte[:1] if isinstance(halte, str) else str(halte)[:1]
    result = requests.get("{0}/{1}/{2}/real-time".format(API_CORE, entiteit, halte))
    return result.json()


def api_search_halte(query: str) -> dict:
    """Api call. Search for halte by name"""
    result = requests.get("{0}/search/haltes/{1}/1".format(API_SEARCH, query))
    return result.json()


def print_doorkomsten(lijnen: dict) -> None:
    """print parsed data in terminal"""
    print("{0} - haltenr: {1}\n".format(lijnen['omschrijvingLang'], lijnen['halteNummer']))
    for item in lijnen['lijnen']:
        realtime = item['vertrekTijd'] if item['predictionStatussen'][0] == "REALTIME" else "GN RT"
        vertrektijd = time.strftime("%H:%M",
                                    time.localtime(item['vertrekTheoretischeTijdstip'] / 1000))

        print("{0} {1:<5}{2:<4}{3:<20}{4:<7}{5}".format(ICON.get(item['lijnType'], ""),
                                                        item['lijnType'], item['lijnNummerPubliek'],
                                                        item['bestemming'], realtime, vertrektijd))


def print_halte_search_results(table: dict) -> None:
    """print parsed data in terminal from 'api_search_halte' function"""
    haltes = table['haltes']
    result = 0
    for halte in haltes:
        result += 1
        lijn_nummers = ", ".join([lijn['lijnNummerPubliek'] for lijn in halte['lijnen']])
        bestemmingen = ", ".join(halte['bestemmingen'])
        print("{0}) {1:<35} - haltenr: {2} - Lijnen: {3} \t Richting: {4}".format(result, halte[
            'omschrijvingLang'], halte['halteNummer'], lijn_nummers, bestemmingen))


def doorkomsten(halte_nummer: str) -> None:
    """Loop for the doorkomsten table"""
    line_filter = None
    while True:
        try:
            data = api_get_doorkomsten(halte_nummer)
            save_query(halte_nummer)
            lijnen = data['halte'][0]
            if line_filter is not None:
                print_doorkomsten(filtered_doorkomsten(line_filter, lijnen))
            else:
                print_doorkomsten(lijnen)
        except (IndexError, TypeError):
            print("Geen doorkomsten gevonden rond huidig tijdstip :-(")
            break

        user_input = input("\nWillekeurige knop = vernieuwen. 0 = opnieuw beginnen, "
                           "f = filter op lijnnr: ")
        os.system('clear')
        if user_input == '0':
            break
        elif user_input == 'f':
            lines = {line['lijnNummerPubliek'] for line in lijnen['lijnen']}
            user_input = input("Kies lijnnr ({0}): ".format(", ".join(lines)))
            if user_input in lines:
                line_filter = user_input


def filtered_doorkomsten(line_filter: str, lijnen: dict) -> dict:
    """filter by a line-nr"""
    lijnen['lijnen'] = [item for item in lijnen['lijnen']
                        if item['lijnNummerPubliek'] == line_filter]
    return lijnen


def save_query(query_input: str) -> None:
    """Put search query in a text file"""
    with open(QUERY_LOG, "w") as file:
        file.write(query_input)


def get_last_query() -> str:
    """Read last search entry from text file"""
    line = ""
    try:
        with open(QUERY_LOG, "r") as file:
            line = file.read()
    except FileNotFoundError:
        pass
    finally:
        return line


def main():
    """
    Script:
    1) Ask user input
    2) User input is haltenr? yes -> get doorkomt info | no -> Search halte by name
    """
    last_query = get_last_query()
    print("######################################")
    print("\U0001F68B \U0001F68C \U0001F68B De lijn doorkomsten \U0001F68C \U0001F68B \U0001F68C")
    print("######################################\n")
    if last_query:
        print("Druk enter om terug halte nr '{0}' op te zoeken".format(last_query))
    else:
        print("\n")

    while True:
        query_input = input("Halte (nr of naam), 0 = afsluiten: ") or last_query
        if query_input == '0':
            break

        last_query = query_input
        try:
            if query_input.isdigit():
                doorkomsten(query_input)
            else:
                data = api_search_halte(query_input)
                if not data['haltes']:
                    print("\nNiets gevonden.probeer een andere zoekterm")
                else:
                    print_halte_search_results(data)
                    user_input = input("\nKies nr. 0 = opnieuw beginnen: ")
                    if user_input != '0':
                        user_input = int(user_input) - 1
                        doorkomsten(data['haltes'][user_input]['halteNummer'])
        except requests.exceptions.RequestException:
            print("Http error! Is there an internet connection?")
            break


if __name__ == '__main__':
    signal(SIGINT, sigint_handler)
    main()
