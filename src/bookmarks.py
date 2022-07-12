"""Dict with favorite stops"""
from dataclasses import dataclass


@dataclass
class Halte:
    bookmark_name: str  # printed on screen
    entiteit: int
    halte_nummer: int


BOOKMARKS = [
    Halte("sint-katelijne", 1, 102700),
    Halte("metro groenplaats -> station", 1, 103756),
    Halte("edenplein -> stad", 1, 102831),
    Halte("folklorelaan -> stad", 1, 102848),
    Halte("groenplaats bus", 1, 102675),
    Halte("borkelstraat -> stad", 1, 105449),
    Halte("amerlolaan -> stad", 1, 101587),
    Halte("weegbreelaan -> stad", 1, 109115),
    Halte("metro diamant -> groenplaats", 1, 103377),
    Halte("metro astrid -> groenplaats", 1, 103364),
    Halte("centraal station -> melkmarkt", 1, 102460)
]
