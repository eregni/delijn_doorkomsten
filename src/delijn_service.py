"""Functions for interacting with De Lijn api's and make urwid.Text objects"""
import urwid

import delijn_repository
from datetime import datetime, timedelta
from tui import ICON


# De lijn search api
def search_halte(search_term: str) -> dict:
    """Search for halte by name or haltenummer"""
    return delijn_repository.zoek_halte(search_term)


def get_halte_search_results_text(haltes_search_result: dict, query: str) -> list[urwid.Text]:
    """Fetch text with urwid markup, parsed from 'api_search_halte' result"""
    # todo fetch more than 10 results?
    nr_of_hits = 10 if haltes_search_result['aantalHits'] > 10 else haltes_search_result['aantalHits']
    urwid_text_list = [urwid.Text(('lightcyan', f"\"{query}\": {nr_of_hits} resultaten"))]
    text_color = 'green'

    halte_data_list = list()
    for halte in haltes_search_result['haltes']:
        result = delijn_repository.get_lijnen_for_halte(halte['haltenummer'], halte['entiteitnummer'])
        halte_data_list.append({
            'haltenummer': halte['haltenummer'],
            'omschrijving': halte['omschrijving'],
            'lijnen': result
        })

    for index, halte in enumerate(halte_data_list):
        lijn_nummers = ", ".join([lijn['lijnnummer'] for lijn in halte['lijnen']['lijnrichtingen']])
        bestemmingen = ", ".join(lijn['bestemming'] for lijn in halte['lijnen']['lijnrichtingen'])
        text = f"{index + 1}) {halte['omschrijving']} - haltenr: "f"{halte['haltenummer']} - " \
               f"Lijnen: {lijn_nummers} Richting: {bestemmingen}"

        urwid_text_list.append(urwid.Text((text_color, text)))
        text_color = 'yellow' if text_color == 'green' else 'green'

    return urwid_text_list


# De lijn core api
def get_doorkomsten(halte_nummer: int, entiteitnummmer: int = None) -> tuple[dict, dict]:
    """Get doorkomsten data"""
    if not entiteitnummmer:
        # so far, im assuming there are nu duplicate haltenummers
        entiteitnummmer = delijn_repository.zoek_halte(str(halte_nummer))['haltes'][0]['entiteitnummer']

    halte = delijn_repository.geef_halte(halte_nummer, entiteitnummmer)
    doorkomsten = delijn_repository.get_doorkomsten_for_halte(int(halte['haltenummer']), int(halte['entiteitnummer']))
    return halte, doorkomsten


def get_doorkomsten_text(halte: dict, doorkomsten: dict) -> list[urwid.Text]:
    """Get formatted string with doorkomsten info"""
    """Fetch text with urwid markup, parsed from get_doorkomsten result"""
    text_list = [urwid.Text(('lightcyan', f"\n{halte['omschrijving']} - haltenr: {doorkomsten['haltenummer']}"))]
    text_color = 'green'
    for doorkomst in doorkomsten['doorkomsten']:
        vertrektijd = datetime.fromisoformat(doorkomst['dienstregelingTijdstip'])
        vertrektijd_text = vertrektijd.strftime('%H:%M')
        delay_text = None

        if 'CANCELLED' in doorkomst['predictionStatussen'] or 'DELETED' in doorkomst['predictionStatussen']:
            realtime_text = ('red', f'{"Rijdt niet":<7}')
        elif 'REALTIME' in doorkomst['predictionStatussen'] and 'real-timeTijdstip' in doorkomst:
            # Sometimes the api doesn't send a 'real-timeTijdstip' even when indicated by prediction status???
            vertrektijd_rt = datetime.fromisoformat(doorkomst['real-timeTijdstip'])
            # set real_time_delta to zero when it appears to be before 'now'. Happens sometimes...
            if vertrektijd_rt <= datetime.now():
                real_time_delta = "0\'"
            else:
                real_time_delta = "{0}\'".format(((vertrektijd_rt - datetime.now()) // 60).seconds)
            realtime_text = (text_color, f"{real_time_delta:<7}")
            if vertrektijd_rt > vertrektijd + timedelta(seconds=60):
                delay = vertrektijd_rt - vertrektijd
                delay_text = ('red', f"+{delay.seconds // 60}\'")
            elif vertrektijd_rt < vertrektijd - timedelta(seconds=60):
                delay = vertrektijd - vertrektijd_rt
                # add an extra min to increase chances of catching your bus...
                delay_text = ('red', f"-{(delay.seconds // 60) + 1}\'")
        else:
            realtime_text = (text_color, f'{"GN RT":<7}')

        lijn_info = delijn_repository.get_lijn(doorkomst['lijnnummer'], halte['entiteitnummer'])
        icon = ICON.get(lijn_info['vervoertype'], "")
        line = [
            (text_color, f"{icon} {lijn_info['vervoertype']:<5}{doorkomst['lijnnummer']:<4}{doorkomst['bestemming']:<20}"),
            realtime_text,
            (text_color, f"{vertrektijd_text:<7}")
        ]

        if delay_text:
            line.append(delay_text)

        text_list.append(urwid.Text(line))
        text_color = 'yellow' if text_color == 'green' else 'green'

    return text_list
