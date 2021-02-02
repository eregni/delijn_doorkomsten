#!/usr/bin/env python3
# Program to show realtime info from 'De lijn'. I wrote this thing because the official
# (android) app works awefully slow on my phone. A solution is to make a program with less
# possibilities:
# search realtime for a specific bus stop by it's nr OR search for bus stop by name

# used/usefull sources:
# API https://delijn.docs.apiary.io/
# https://data.delijn.be
# https://github.com/bollewolle/pydelijn/blob/master/pydelijn
#
import requests
import time


BASEURL = 'https://api.delijn.be/DLKernOpenData/api/v1'
API_KEY = {'Ocp-Apim-Subscription-Key': '2219b59ff6d84b5a9a4bc5e971b36436'}
ICON = {
    'bus': '\U0001F68C',
    'tram': '\U0001F68B',
    'metro': '\U0001F687',
}


def get_doorkomst(halte: str) -> dict:
    """Make api call"""
    entiteit = halte[:1]
    r_realtime = requests.get('{0}/haltes/{1}/{2}/real-time'.format(BASEURL, entiteit, halte),  headers=API_KEY)
    r_dienstregeling = requests.get('{0}/haltes/{1}/{2}/dienstregelingen'.format(BASEURL, entiteit, halte),
                                    headers=API_KEY)
    r_halte = requests.get('{0}/haltes/{1}/{2}'.format(BASEURL, entiteit, halte), headers=API_KEY)
    tables = {'realtime': r_realtime.json(), 'dienstregeling': r_dienstregeling.json(), 'halte': r_halte.json()}
    return tables


def print_tui(table: dict) -> None:
    """
    print parsed data in terminal
    Possible types of data
    1: doorkomsten voor specifieke halte
    2: zoekresultaat met haltes
    """
    rt_table = table['realtime']['halteDoorkomsten'][0]
    dienst = table['dienstregeling']['halteDoorkomsten'][0]
    halte = table['halte']

    # TODO| I GIVE UP! I hate this new API!!! I need 4 api calls to get the same data wich I used to get with one call
    # TODO| THIS IS NO PROGRESS! ONLY EVER EXPANDING CODE!
    print('{0} - haltenr: {1}\n'.format(halte['omschrijving'], halte['haltenummer']))
    for item in rt_table['doorkomsten']:
        realtime = item['real-timeTijdstip'] if item['predictionStatussen'][0] == 'REALTIME' else 'GN RT'
        vertrektijd = time.strftime('%H:%M', time.localtime(item['dienstregelingTijdstip']))

        print('{0} {1:<5}{2:<4}{3:<20}{4:<7}{5}'.format(ICON.get(item['lijnType'], 'bus'), item['lijnType'],
                                                        item['lijnNummerPubliek'], item['bestemming'], realtime,
                                                        vertrektijd))


def tui():
    # halte_nr = input('Geef haltenr: ')
    halte_nr = '102848'
    if halte_nr.isdigit():
        print_tui(get_doorkomst(halte_nr))
    else:
        pass  # todo search halte and fetch results

    input('Druk op enter om af te sluiten...')


# for now we are just using the old, fancy terminal
tui()
