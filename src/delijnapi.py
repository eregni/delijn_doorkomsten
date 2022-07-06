"""
Collection of api calls
docs: https://data.delijn.be/docs/services/
"""
from enum import Enum
import requests
from requests import Response
from models import HaltesHits, Halte, Link, GeoCoordinaat, Lijnrichtingen

TIMEOUT = 5  # timeout in seconds


class Endpoints(Enum):
    DL_CORE = 'https://api.delijn.be/DLKernOpenData/api/v1'
    DL_SEARCH = 'https://api.delijn.be/DLZoekOpenData/v1'

try:
    with open('api_key.txt', 'r') as f:
        API_KEY = f.readline()
except FileNotFoundError:
    pass  # TODO handle exception


def zoek_haltes(zoek_argument: str, huidige_positie: str = None, start_index: int = 0, max_aantal_hits: int = 10) -> HaltesHits:
    params = {'huidigePositie': huidige_positie, "startIndex": start_index, 'maxAantalHits': max_aantal_hits}
    path = f"/zoek/haltes/{zoek_argument}"
    result = _call_api(path, Endpoints.DL_SEARCH, params)
    return result.json(object_hook=HaltesHits)


def api_get_list_lijn_richtingen(haltesleutels: str) -> Response:
    path = f"/haltes/lijst/{haltesleutels}/lijnrichtingen"
    result = _call_api(path, Endpoints.DL_CORE)
    return result.json(object_hook=Lijnrichtingen)








# old api



def api_get_doorkomsten(halte: int, num_results: int = 10) -> [dict, str]:
    """Get realtime info from halte"""
    halte_search = api_search_halte(halte)
    if len(halte_search['haltes']) != 1:
        return "Doorkomsten nr haltes != 1 -> time to review the code..."  # todo: is the haltenr unique?

    entiteit = halte_search['haltes'][0]['entiteitnummer']
    url = f"{API_CORE}/haltes/{entiteit}/{halte}/real-time?maxAantalDoorkomsten=10"
    return _call_api(url)

# end old api


def _call_api(path: str, endpoint: Endpoints, params: dict = None) -> Response:
    """Call Api"""
    headers = {'Ocp-Apim-Subscription-Key': API_KEY}
    try:
        result = requests.get(f"{endpoint.value}{path}", params=params, headers=headers, timeout=TIMEOUT)
        if result.status_code != 200:
            raise DelijnApiError(result)

        return result

    except requests.ConnectionError:
        raise DelijnApiError("Timeout. Is there an internet connection?")


class DelijnApiError(Exception):
    def __init__(self, response: [Response, str]):
        if isinstance(response, Response):
            parsed = response.json()
            self.message = f"server response {parsed['statusCode']}: {parsed['message']}"
        else:
            self.message = response
        super().__init__(self.message)

