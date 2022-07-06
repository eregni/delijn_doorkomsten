# mapping json to python objects -> https://www.geeksforgeeks.org/convert-nested-python-dictionary-to-object/
# Models
from enum import Enum


class GeoCoordinaat:
    def __init__(self, json_dict: dict):
        self.__dict__.update(json_dict)
        self.latitude: float = 0.0
        self.longitude: float = 90.0


class Link:
    def __init__(self, json_dict: dict):
        self.__dict__.update(json_dict)
        self.rel: str = ""
        self.url: str = ""


class Halte:
    def __init__(self, json_dict: dict):
        self.__dict__.update(json_dict)
        self.entiteitnummer: str
        self.haltenummer: str
        self.omschrijving: str
        self.gemeentenummer: str
        self.omschrijvingGemeente: str
        self.geoCoordinaat: GeoCoordinaat
        self.links: list[Link] = []


class HaltesHits:
    def __init__(self, json_dict: dict):
        self.__dict__.update(json_dict)
        self.aantalHits: int
        self.haltes: list[Halte]


class Lijnrichtingen:
    def __init__(self, json_dict: dict):
        self.__dict__.update(json_dict)
        self.lijnrichtingen: list[LijnRichting] = []
        self.links = list[Link]


class LijnRichting:
    def __init__(self, json_dict: dict):
        self.__dict__.update(json_dict)
        self.lijnNummerPubliek: str = ""
        self.entiteitnummer: str
        self.lijnnummer: str
        self.richting: Richting
        self.omschrijving: str
        self.bestemming: str = "LEUVEN GASTHUISB."
        self.kleurVoorGrond: str = "#FFFFFF"
        self.kleurAchterGrond: str = "#991199"
        self.kleurAchterGrondRand: str = "#991199"
        self.links: list[Link] = []


class Richting(Enum):
    HEEN = "HEEN",
    TERUG = "TERUG"
