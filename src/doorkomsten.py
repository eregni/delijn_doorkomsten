#!/usr/bin/env python3
"""
Program to show realtime info from De lijn. I wrote this thing because the official
(android) app works awefully slow on my phone. A solution is to make a terminal program with
(a lot) less feautures:

*   search realtime info for a specific bus stop. When there's no result search for
    a stop by name

*   Filter search results by line nr

I've used dutch words in the code and comments because I kept the same variable names as found in
the api from De Lijn

usefull sources:
API https://delijn.docs.apiary.io/
todo: use new api -> https://data.delijn.be
todo: storing op lijn melden?
todo: bug filter by line
todo: vertraging in tabel zetten
"""
import time
import sys
from signal import signal, SIGINT
import requests
#  List with favorite stops
FAVORITES = [
    ("sint-katelijne", 102700),
    ("metro groenplaats -> station", 103756),
    ("edenplein -> stad", 102831),
    ("folklorelaan -> stad", 102848, 
    ("groenplaats bus", 102675),
    ("borkelstraat -> stad", 105449),
    ("amerlolaan -> stad", 101587),
    ("weegbreelaan -> stad", 109115),
    ("metro diamant -> groenplaats", 103377),
    ("metro astrid -> groenplaats", 103364),
    ("centraal station -> melkmarkt", 102460),
]
QUERY_LOG = "search.txt"
API_CORE = 'https://www.delijn.be/rise-api-core/haltes/vertrekken'
API_SEARCH = 'https://www.delijn.be/rise-api-search'
ICON = {
    'bus': '\U0001F68C',
    'tram': '\U0001F68B',
    'metro': '\U0001F687',
}


# https://www.geeksforgeeks.org/print-colors-python-terminal/
class Colors:
    """Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold"""
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class Fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class Bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'


def sigint_handler(sig, frame):
    """Handler for SIGINT signal"""
    print("\nctrl-c. Bye!")
    sys.exit(0)


def api_get_doorkomsten(halte):
    """Api call. Get realtime info from halte"""
    entiteit = str(halte)[:1]
    try:
        result = requests.get("{0}/{1}/{2}/real-time".format(API_CORE, entiteit, halte))
        data = request_to_json(result)
        return data
    except requests.ConnectionError:
        print("Http error! Is there an internet connection?")


def api_search_halte(query):
    """Api call. Search for halte by name"""
    try:
        result = requests.get("{0}/search/haltes/{1}/1".format(API_SEARCH, query))
        data = request_to_json(result)
        return data
    except requests.ConnectionError:
        print("Http error! Is there an internet connection?")


def request_to_json(data):
    """Catch json decode exceptions"""
    try:
        return data.json()
    except ValueError:  # should catch json decode exceptions
        return None


def print_doorkomsten(lijnen):
    """print parsed data in terminal"""
    text_color = Colors.Fg.lightblue
    print("\n{2}{0} - haltenr: {1}".format(lijnen['omschrijvingLang'], lijnen['halteNummer'], text_color))
    text_color = Colors.Fg.lightgreen
    for item in lijnen['lijnen']:
        realtime = item['vertrekTijd'] if item['predictionStatussen'][0] == "REALTIME" else "GN RT"
        vertrektijd = time.strftime("%H:%M",
                                    time.localtime(item['vertrekTheoretischeTijdstip'] / 1000))

        print("{6}{0} {1:<5}{2:<4}{3:<25}{4:<7}{5}".format(ICON.get(item['lijnType'], ""),
                                                        item['lijnType'], item['lijnNummerPubliek'],
                                                        item['bestemming'], realtime, vertrektijd,
                                                           text_color))
        if text_color == Colors.Fg.lightgreen:
            text_color = Colors.Fg.yellow
        else:
            text_color = Colors.Fg.lightgreen

    print(Colors.reset)


def print_halte_search_results(table, query):
    """print parsed data in terminal from 'api_search_halte' function"""
    text_color = Colors.Fg.lightblue
    print("\n{0}\"{1}\"".format(text_color, query))
    text_color = Colors.Fg.lightgreen
    haltes = table['haltes']
    result = 0
    for halte in haltes:
        result += 1
        lijn_nummers = ", ".join([lijn['lijnNummerPubliek'] for lijn in halte['lijnen']])
        bestemmingen = ", ".join(halte['bestemmingen'])
        print("{5}{0}) {1} - haltenr: {2} - Lijnen: {3} Richting: {4}".format(result, halte[
            'omschrijvingLang'], halte['halteNummer'], lijn_nummers, bestemmingen, text_color))

        if text_color == Colors.Fg.lightgreen:
            text_color = Colors.Fg.yellow
        else:
            text_color = Colors.Fg.lightgreen

    print(Colors.reset)


def doorkomsten(halte_nummer):
    """Loop for the doorkomsten table"""
    line_filter = None
    while True:
        try:
            data = api_get_doorkomsten(halte_nummer)
            lijnen = data['halte'][0]
            if line_filter is not None:
                print_doorkomsten(filtered_doorkomsten(line_filter, lijnen))
            else:
                print_doorkomsten(lijnen)
        except (IndexError, TypeError):
            print("Geen doorkomsten gevonden rond huidig tijdstip :-(")
            break

        user_input = input("Willekeurige knop = vernieuwen. 0 = opnieuw beginnen, "
                           "f = filter op lijnnr: ")
        if user_input == '0':
            break
        elif user_input == 'f':
            lines = {line['lijnNummerPubliek'] for line in lijnen['lijnen']}
            user_input = input("Kies lijnnr ({0}): ".format(", ".join(lines)))
            if user_input in lines:
                line_filter = user_input


def filtered_doorkomsten(line_filter, lijnen):
    """filter by a line-nr"""
    lijnen['lijnen'] = [item for item in lijnen['lijnen']
                        if item['lijnNummerPubliek'] == line_filter]
    return lijnen


def save_query(query_input):
    """Put search query in a text file"""
    with open(QUERY_LOG, "w") as file:
        file.write(str(query_input))


def get_last_query():
    """Read last search entry from text file"""
    line = ""
    try:
        with open(QUERY_LOG, "r") as file:
            line = file.read()
    except FileNotFoundError:
        pass
    finally:
        return line


def search_halte(query):
    data = api_search_halte(query)
    if data is None:
        return
    if not data['haltes']:
        print("\nNiets gevonden.probeer een andere zoekterm")
    else:
        print_halte_search_results(data, query)
        user_input = input("\nKies nr. 0 = opnieuw beginnen: ")
        if user_input != '0' and user_input.isdigit():
            user_input = int(user_input) - 1
            haltenr = data['haltes'][user_input]['halteNummer']
            doorkomsten(haltenr)
            return str(haltenr)
        else:
            print("Ongeldige invoer")


def query_favorites():
    print(Colors.Fg.lightblue)
    index = 1
    for stop, nr in FAVORITES:
        print(f"{index}) {stop} ({nr})")
        index += 1

    user_input = input(f"{Colors.reset}Kies nr: ")
    if user_input.isdigit():
        try:
            _, halte = FAVORITES[int(user_input) - 1]
            doorkomsten(halte)
            return str(halte)
        except IndexError:
            print("Ongeldige keuze")
            return None


def main():
    """
    Script:
    1) Ask user input
    2) User input is
        int/haltenr -> get doorkomt info
        string      -> Search halte by name
        'f'         -> list favorite stops
        '0'         -> exit script
    """
    last_query = get_last_query()
    print("######################################")
    print("\U0001F68B \U0001F68C \U0001F68B De lijn doorkomsten \U0001F68C \U0001F68B \U0001F68C")
    print("######################################\n")

    while True:
        if last_query:
            print("Druk enter om '{0}' op te zoeken".format(last_query))

        user_input = input("Halte (nr of naam), f = favorieten, 0 = afsluiten: ") or last_query
        if user_input == '0':
            break

        if user_input == '':
            continue

        if user_input == 'f':
            last_query = query_favorites()
            if last_query is not None:
                save_query(last_query)

        elif user_input.isdigit():
            last_query = user_input
            doorkomsten(user_input)

        else:
            last_query = search_halte(user_input)
            if last_query is not None:
                save_query(last_query)


if __name__ == '__main__':
    signal(SIGINT, sigint_handler)
    main()
