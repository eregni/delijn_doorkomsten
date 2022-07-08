"""
Collection of api calls
docs: https://data.delijn.be/docs/services/
"""
import exceptions

from delijn_api_kern import exceptions as kern_exceptions, Configuration as KernConfiguration, ApiClient as KernApiClient
from delijn_api_kern.model.lijnrichtingen import Lijnrichtingen
from delijn_api_kern.model.lijnrichting import Lijnrichting
from delijn_api_kern.model.ritten import Ritten
from delijn_api_kern.api.haltes_api import HaltesApi
from delijn_api_kern.api.lijnen_api import LijnenApi

from delijn_api_zoek import exceptions as zoek_exceptions, Configuration as ZoekConfiguration, ApiClient as ZoekApiClient
from delijn_api_zoek.model.haltes_hits import HaltesHits
from delijn_api_zoek.api.zoeken_api import ZoekenApi


try:
    with open('api_key.txt', 'r') as f:
        key = f.readline()
        api_key = {'apiKeyHeader': key, 'apiKeyQuery': key}
except FileNotFoundError:
    print('You need a file with you api key from https://data.delijn.be/signin')

DELIJN_KERN_CONFIG = KernConfiguration(api_key=api_key)
DELIJN_ZOEK_CONFIG = ZoekConfiguration(api_key=api_key)


def zoek_halte(zoek_argument: str, huidige_positie: str = None, start_index: int = 0,
               max_aantal_hits: int = 10) -> HaltesHits:
    """Search for halte by keyword"""
    with ZoekApiClient(configuration=DELIJN_ZOEK_CONFIG) as api_client:
        api_instance = ZoekenApi(api_client)
        args = {'start_index': start_index, 'max_aantal_hits': max_aantal_hits}
        if huidige_positie:
            args['huidige_positie'] = huidige_positie

        try:
            result: HaltesHits = api_instance.zoek_haltes(zoek_argument, **args)
        except zoek_exceptions.OpenApiException as ex:
            raise exceptions.DelijnApiError(ex)
        return result


# todo CONTINUE here: api definition is invalid again (and again...). Time to reverse engineer it...
def geef_halte(halte_nr: int, entiteit_nr: int):
    """Get halte by haltenummer"""
    with KernApiClient(configuration=DELIJN_KERN_CONFIG) as api_client:
        api_instance = HaltesApi(api_client)
        try:
            result = api_instance.geef_halte(entiteit_nr, halte_nr)
        except kern_exceptions.OpenApiException as ex:
            raise exceptions.DelijnApiError(ex)
        return result



def get_lijnen_for_halte(halte_nr: int, eniteit_nr: int):
    raise NotImplementedError


def get_lijnen_for_haltes(haltesleutels: str) -> Lijnrichtingen:
    """Get list of lines from halte"""
    raise NotImplementedError
    # with KernApiClient(configuration=DELIJN_KERN_CONFIG) as api_client:
    #     api_instance = HaltesApi(api_client)
    #     try:
    #         result: HalteLijnRichtingen  = api_instance.geef_halte_lijnrichtingen_lijst(haltesleutels)  # todo api is out of date! There is no return object 'HalteLijnRichtingen' specified
    #     except kern_exceptions.OpenApiException as ex:
    #         raise exceptions.DelijnApiError(ex)
    #     return result


def get_doorkomsten_for_halte(halte_nr: int, entiteit_nr: int, max_aantal_doorkomsten: int = 10) -> Ritten:
    """Get the realtime info from halte"""
    with KernApiClient(configuration=DELIJN_KERN_CONFIG) as api_client:
        api_instance = HaltesApi(api_client)
        try:
            result = api_instance.geef_doorkomsten_voor_halte(entiteit_nr, halte_nr, max_aantal_doorkomsten=max_aantal_doorkomsten)
        except kern_exceptions.OpenApiException as ex:
            raise exceptions.DelijnApiError(ex)
        return result

