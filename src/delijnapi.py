"""
Collection of api calls
docs: https://data.delijn.be/docs/services/
"""
from typing import Union
import requests

API_CORE = 'https://api.delijn.be/DLKernOpenData/api/v1'
API_SEARCH = 'https://api.delijn.be/DLZoekOpenData/v1'
API_USER = 'eregni'
API_KEY = '2219b59ff6d84b5a9a4bc5e971b36436'  # TODO remove api key!!!
API_KEY2 = 'f66c83682a6a418884fcb4fb8a43e5f4'
TIMEOUT = 5


def _call_api(url: str) -> Union[dict, str]:
    """Call Api"""
    headers = {'Ocp-Apim-Subscription-Key': API_KEY}
    try:
        result = requests.get(f"{url}", headers=headers, timeout=TIMEOUT)
        return result.json()
    except requests.ConnectionError:
        return 'timeout'
    except ValueError:
        pass  # silence json decode exceptions


def api_get_doorkomsten(halte: int, num_results: int = 10) -> [dict, str]:
    """Get realtime info from halte"""
    halte_search = api_search_halte(halte)
    if len(halte_search['haltes']) != 1:
        return "Doorkomsten nr haltes != 1 -> time to review the code..."  # todo: is the haltenr unique?

    entiteit = halte_search['haltes'][0]['entiteitnummer']
    url = f"{API_CORE}/haltes/{entiteit}/{halte}/real-time?maxAantalDoorkomsten=10"
    return _call_api(url)


def api_get_list_lijn_richtingen(haltes: tuple[tuple[str, str]]) -> dict:
    halte_sleutels = '_'.join(tuple(f'{halte[0]}_{halte[1]}' for halte in haltes))
    url = f"{API_CORE}/haltes/lijst/{halte_sleutels}/lijnrichtingen"
    return _call_api(url)


def api_search_halte(query: [str, int]) -> dict:
    """Api call. Search for halte by name"""
    # TODO search by fetched gps coordinates
    url = f"{API_SEARCH}/zoek/haltes/{query}?maxAantalHits=10"
    return _call_api(url)

