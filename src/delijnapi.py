"""
Collection of api calls
API https://delijn.docs.apiary.io/
"""
import requests

API_CORE = 'https://www.delijn.be/rise-api-core'
API_SEARCH = 'https://www.delijn.be/rise-api-search'


def call_api(url: str) -> dict:
    """Call Api"""
    try:
        result = requests.get(f"{url}")
        return result.json()
    except requests.ConnectionError:
        pass  # todo Find out how to pass on exceptions properly. (Silencing this triggers a TypeError later in doorkomsten function
    except ValueError:
        pass  # silence json decode exceptions


def api_get_doorkomsten(halte: int, num_results: int = 10):
    """Get realtime info from halte"""
    url = f"{API_CORE}/haltes/vertrekken/{halte}/{num_results}"
    return call_api(url)


def api_search_halte(query: str):
    """Api call. Search for halte by name"""
    url = f"{API_SEARCH}/search/haltes/{query}/1"  # the '1' is an unknown parameter 'publication_id'
    return call_api(url)
