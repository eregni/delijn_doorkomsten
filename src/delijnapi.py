"""
Collection of api calls
API https://delijn.docs.apiary.io/
"""
from typing import Union
import requests

API_CORE = 'https://www.delijn.be/rise-api-core'
API_SEARCH = 'https://www.delijn.be/rise-api-search'
TIMEOUT = 5


def _call_api(url: str) -> Union[dict, str]:
    """Call Api"""
    try:
        result = requests.get(f"{url}", timeout=TIMEOUT)
        return result.json()
    except requests.ConnectionError:
        return 'timeout'
    except ValueError:
        pass  # silence json decode exceptions


def api_get_doorkomsten(halte: int, num_results: int = 10):
    """Get realtime info from halte"""
    url = f"{API_CORE}/haltes/vertrekken/{halte}/{num_results}"
    return _call_api(url)


def api_search_halte(query: str):
    """Api call. Search for halte by name"""
    url = f"{API_SEARCH}/search/haltes/{query}/1"  # the '1' is an unknown parameter 'publication_id'
    return _call_api(url)
