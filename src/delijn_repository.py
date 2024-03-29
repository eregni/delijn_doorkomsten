"""
Collection of api calls
docs: https://data.delijn.be/docs/services/
function comment are in Dutch -> copied from the api definition
"""
from time import sleep
from pathlib import Path
import requests

API_KEY_PATH = 'api_key.txt'
DL_CORE = 'https://api.delijn.be/DLKernOpenData/api/v1'
DL_SEARCH = 'https://api.delijn.be/DLZoekOpenData/v1'

try:
    with open(Path.joinpath(Path(__file__).parent.absolute(), API_KEY_PATH), 'r') as f:
        key = f.readline().strip()
        API_KEY = {'Ocp-Apim-Subscription-Key': key}
except FileNotFoundError:
    print(f"You need a file \'{API_KEY_PATH}\' with you api key from https://data.delijn.be/signin")
    raise SystemExit


# De lijn search api
def zoek_halte(zoek_argument: str, huidige_positie: str = None, start_index: int = 0, max_aantal_hits: int = 10) -> dict:
    """Search for halte by keyword"""

    url = f"{DL_SEARCH}/zoek/haltes/{zoek_argument}"
    params = {'maxAantalHits': max_aantal_hits}
    if huidige_positie:
        params['huidigePositie'] = huidige_positie
    if start_index:
        params['startIndex'] = start_index

    result = _call_api(url, params)
    return result.json()


# De lijn core api
def geef_halte(halte_nr: int, entiteit_nr: int) -> dict:
    """Geef een halte op basis van het opgegeven haltenummer"""
    url = f"{DL_CORE}/haltes/{entiteit_nr}/{halte_nr}"
    result = _call_api(url)
    return result.json()


def geef_haltes(halte_keys: str) -> dict:
    """Geef een lijst van haltes op basis van een lijst van halte sleutels"""
    url = f"{DL_CORE}/haltes/lijst/{halte_keys}"
    result = _call_api(url)
    return result.json()


def geef_lijnen_voor_halte(halte_nr: int, entiteit_nr: int) -> dict:
    """Geef de lijnrichtingen die de opgegeven halte bedienen"""
    url = f"{DL_CORE}/haltes/{entiteit_nr}/{halte_nr}/lijnrichtingen"
    result = _call_api(url)
    return result.json()


def geef_lijnen_voor_haltes(halte_sleutels: str) -> dict:
    """
    Geef de lijnrichtingen die de opgegeven halte bedienen op basis van een lijst van halte sleutels.
    Max 8 sleutels
    """
    url = f"{DL_CORE}/haltes/lijst/{halte_sleutels}/lijnrichtingen"
    result = _call_api(url)
    return result.json()


def geef_doorkomsten_voor_halte(halte_nr: int, entiteit_nr: int, max_aantal_doorkomsten: int = 10) -> dict:
    """Geef de real-time doorkomsten voor de opgegeven halte sleutels"""
    url = f"{DL_CORE}/haltes/{entiteit_nr}/{halte_nr}/real-time"
    params = {'maxAantalDoorkomsten': max_aantal_doorkomsten}
    result = _call_api(url, params=params)
    return result.json()


def geef_doorkomsten_voor_haltes(halte_sleutels: str, max_aantal_doorkomsten: int = 10) -> dict:
    """Geef de real-time doorkomsten voor de opgegeven halte sleutels"""
    url = f"{DL_CORE}/haltes/lijst/{halte_sleutels}/realtime"
    params = {'max_aantal_doorkomsten': max_aantal_doorkomsten}
    result = _call_api(url, params=params)
    return result.json()


def geef_lijn(lijn_nr: int, entiteit_nr: int) -> dict:
    """Geef een lijn op basis van het opgegeven lijnnummer"""
    url = f"{DL_CORE}/lijnen/{entiteit_nr}/{lijn_nr}"
    result = _call_api(url)
    return result.json()


def geef_lijnen(lijn_sleutels: str):
    """
    Geef een lijst van lijnen op basis van een lijst van lijn sleutels.
    lijn sleutel -> str({entiteitnummer}_{lijnnummer})
    """
    url = f"{DL_CORE}/lijnen/lijst/{lijn_sleutels}"
    result = _call_api(url)
    return result.json()


def _call_api(url: str, params: dict = None):
    """Call the api"""
    while True:
        result = requests.get(url, params, headers=API_KEY)
        # Pauze when the server get irritated
        if result.status_code == 429:
            sleep(2)
            continue

        elif result.status_code != 200:
            raise requests.RequestException

        break

    return result
