"""Collection of api calls"""
import requests

API_CORE = 'https://www.delijn.be/rise-api-core'
API_SEARCH = 'https://www.delijn.be/rise-api-search'


def call_api(url: str) -> dict:
    """Call Api"""
    try:
        result = requests.get(f"{url}")
        return result.json()
    except requests.ConnectionError:
        print("Http error!; Is there an internet connection?")
    except ValueError:
        pass  # silence json decode exceptions


def api_get_doorkomsten(halte: int):
    """Get realtime info from halte"""
    url = f"{API_CORE}/haltes/vertrekken/{halte}"
    return call_api(url)


def api_search_halte(query: str):
    """Api call. Search for halte by name"""
    url = f"{API_SEARCH}/search/haltes/{query}/1"  # the '1' is an unknown parameter 'publication_id'
    return call_api(url)
