"""Functions for interacting with De Lijn api's"""
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
    urwid_text_list = [urwid.Text(('lightcyan', f"\"{query}\": {haltes_search_result['aantalHits']} resultaten"))]
    text_color = 'green'

    halte_keys = '_'.join(
        [f"{halte['entiteitnummer']}_{halte['haltenummer']}" for halte in haltes_search_result['haltes']])

    lijnen_bij_haltes = delijn_repository.get_lijnen_for_haltes(halte_keys)
    for index, halte in enumerate(lijnen_bij_haltes['halteLijnrichtingen']):
        lijn_nummers = ", ".join([lijn['lijnnummer'] for lijn in halte['lijnrichtingen']])
        bestemmingen = ", ".join(lijn['bestemming'] for lijn in halte['lijnrichtingen'])
        halte_omschrijving = ""
        for _halte in haltes_search_result['haltes']:
            if _halte['haltenummer'] == halte['halte']['haltenummer']:
                halte_omschrijving = _halte['omschrijving']
                break

        text = f"{index + 1}) {halte_omschrijving} - haltenr: "f"{halte['halte']['haltenummer']} - " \
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
    text_list = [('lightcyan', f"\n{halte['omschrijving']} - haltenr: {doorkomsten['haltenummer']}")]
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
            realtime_text = (text_color, f"{vertrektijd_rt.strftime('%H:%M'):<7}")
            if vertrektijd_rt > vertrektijd + timedelta(seconds=60):
                delay = vertrektijd_rt - vertrektijd
                delay_text = ('red', f"+{delay.seconds // 60}\'\n")
            elif vertrektijd_rt < vertrektijd - timedelta(seconds=60):
                delay = vertrektijd - vertrektijd_rt
                # add an extra min to increase chances of catching your bus...
                delay_text = ('red', f"-{(delay.seconds // 60) + 1}\'\n")
        else:
            realtime_text = (text_color, f'{"GN RT":<7}')

        lijn_info = delijn_repository.get_lijn(doorkomst['lijnnummer'], halte['entiteitnummer'])
        icon = ICON.get(lijn_info['vervoertype'], "")
        line = [
            (text_color,
             f"{icon} {lijn_info['vervoertype']:<5}{doorkomst['lijnnummer']:<4}{doorkomst['bestemming']:<20}"),
            realtime_text,
            (text_color, f"{vertrektijd_text:<7}"),
            '\n' if delay_text is None else delay_text]

        text_list.append(line)
        text_color = 'yellow' if text_color == 'green' else 'green'

    return text_list
