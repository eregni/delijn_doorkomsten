"""Functions for interacting with De Lijn api's and make urwid.Text objects"""
from urwid import Text

import delijn_repository
from datetime import datetime, timedelta
from models.tui import ICON


# De lijn search api
def search_halte(search_term: str) -> dict:
    """Search for halte by name or haltenummer"""
    return delijn_repository.zoek_halte(search_term)


def get_halte_search_results_text(haltes_search_result: dict, query: str) -> list[Text]:
    """Fetch text with urwid markup, parsed from 'api_search_halte' result"""
    # todo fetch more than 10 results? -> create <more> Button
    nr_of_hits = 10 if haltes_search_result['aantalHits'] > 10 else haltes_search_result['aantalHits']
    haltes = haltes_search_result['haltes']
    text_color = 'green'

    # De lijn API gives results for max 8 haltes at once, so we split out list up in groups
    halte_sleutels = "_".join([f"{halte['entiteitnummer']}_{halte['haltenummer']}" for halte in haltes])
    results = delijn_repository.geef_lijnen_voor_haltes(halte_sleutels)

    urwid_text_list = [Text(('lightcyan', f"\"{query}\": {len(results['halteLijnrichtingen'])} resultaten"))]
    for index, data in enumerate(results['halteLijnrichtingen']):
        lijn_nummers = ", ".join([lijn['lijnnummer'] for lijn in data['lijnrichtingen']])
        bestemmingen = ", ".join(lijn['bestemming'] for lijn in data['lijnrichtingen'])
        omschrijving = next(halte['omschrijving']
                            for halte in haltes if halte['haltenummer'] == data['halte']['haltenummer'])
        text = f"{index + 1}) {omschrijving} - haltenr: "f"{data['halte']['haltenummer']} - Lijnen: {lijn_nummers} " \
               f"Richting: {bestemmingen}"
        urwid_text_list.append(Text((text_color, text)))

        text_color = 'yellow' if text_color == 'green' else 'green'

    return urwid_text_list


# De lijn core api
def get_doorkomsten(halte_nummer: str, entiteitnummmer: str = None) -> tuple[dict, dict]:
    """Get doorkomsten data"""
    if not entiteitnummmer:
        # so far, im assuming there are no duplicate haltenummers
        entiteitnummmer = delijn_repository.zoek_halte(halte_nummer)['haltes'][0]['entiteitnummer']

    halte = delijn_repository.geef_halte(int(halte_nummer), int(entiteitnummmer))
    doorkomsten = delijn_repository.geef_doorkomsten_voor_halte(int(halte['haltenummer']), int(halte['entiteitnummer']))
    return halte, doorkomsten


def get_doorkomsten_text(halte: dict, doorkomsten: dict) -> list[Text]:
    """Get formatted Text with doorkomsten info"""
    """Fetch text with urwid markup, parsed from get_doorkomsten result"""
    text_list = [Text(('lightcyan', f"{halte['omschrijving']} - haltenr: {doorkomsten['haltenummer']}"))]
    text_color = 'green'

    lijn_sleutels = [f"{item['entiteitnummer']}_{item['lijnnummer']}" for item in doorkomsten['doorkomsten']]
    lijn_sleutels = "_".join(list(dict().fromkeys(lijn_sleutels)))
    lijnen_data = delijn_repository.geef_lijnen(lijn_sleutels)

    for doorkomst in doorkomsten['doorkomsten']:
        # It happened there is a 'doorkomst' without any time/real-time info. In that case the info is useless
        # so we drop it..
        if 'dienstregelingTijdstip' not in doorkomst and 'GEENREALTIME' in doorkomst['predictionStatussen']:
            continue

        vertrektijd = datetime.fromisoformat(doorkomst['dienstregelingTijdstip'])
        vertrektijd_text = vertrektijd.strftime('%H:%M')
        delay_text = None

        cancelled_status = ('CANCELLED', 'DELETED', 'GESCHRAPT')
        if any(status in cancelled_status for status in doorkomst['predictionStatussen']):
            realtime_text = ('red', f'{"Rijdt niet":<11}')
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

        vervoer_type = next(
            lijn['vervoertype'] for lijn in lijnen_data['lijnen']
            if int(lijn['lijnnummer']) == doorkomst['lijnnummer'])
        icon = ICON.get(vervoer_type)
        text_line = [
            (text_color, f"{icon} {vervoer_type:<5}{doorkomst['lijnnummer']:<4}{doorkomst['bestemming']:<20}"),
            realtime_text,
            (text_color, f"{vertrektijd_text:<7}")
        ]

        if delay_text:
            text_line.append(delay_text)

        text_list.append(Text(text_line))
        text_color = 'yellow' if text_color == 'green' else 'green'

    return text_list
