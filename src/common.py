"""Commonly used functions"""


def get_lines_from_doorkomsten(doorkomsten: dict) -> list[str]:
    """Give a list containing the line nrs from the doorkomsten data returned by delijn api"""
    lines = [line['lijnnummer'] for line in doorkomsten['doorkomsten']]
    lines = list(dict.fromkeys(lines))
    lines.sort()
    return list(map(str, lines))
