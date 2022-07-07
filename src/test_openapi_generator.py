from enum import Enum
from time import perf_counter
import requests
from pprint import pprint

import delijn_api_zoek
from delijn_api_zoek.api import zoeken_api


class Endpoints(Enum):
    DL_CORE = 'https://api.delijn.be/DLKernOpenData/api/v1'
    DL_SEARCH = 'https://api.delijn.be/DLZoekOpenData/v1'


iterations = 50
search_term = '102700'

with open('api_key.txt', 'r') as f:
    api_key = f.readline()

configuration = delijn_api_zoek.Configuration(api_key={'apiKeyHeader': api_key,'apiKeyQuery': api_key})
# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = api_key
# Configure API key authorization: apiKeyQuery
configuration.api_key['apiKeyQuery'] = api_key

start = perf_counter()
for i in range(iterations):
    with delijn_api_zoek.ApiClient(configuration=configuration) as api_client:
        api_instance = zoeken_api.ZoekenApi(api_client)
        result = api_instance.zoek_haltes(search_term)
        # pprint(result)

timing = perf_counter() - start
print(f"Timing openapi-generator: {timing} -> {round(iterations / timing, 2)} calls/sec")

start = perf_counter()
for i in range(iterations):
    result = requests.get(f'{Endpoints.DL_SEARCH.value}/zoek/haltes/{search_term}', timeout=5, headers={'Ocp-Apim-Subscription-Key': api_key})
    # pprint(result.json())

timing = perf_counter() - start
print(f"Timing plain requests: {timing} -> {round(iterations / timing, 2)} calls/sec")

