from pprint import pprint
from time import perf_counter
import delijn_api_kern.apis
import delijn_api_zoek.apis

with open('api_key.txt', 'r') as f:
    api_key = f.readline()
start = perf_counter()
for i in range(50):
    with delijn_api_kern.ApiClient(header_name='Ocp-Apim-Subscription-Key', header_value=api_key) as api_client:
        api_instance = delijn_api_kern.apis.OmleidingenApi(api_client)
        result = api_instance.geef_omleidingen()
        pprint(result)
print(perf_counter() - start)

start = perf_counter()
for i in range(50):
    with delijn_api_zoek.ApiClient(header_name='Ocp-Apim-Subscription-Key', header_value=api_key) as api_client:
        api_instance = delijn_api_zoek.apis.ZoekenApi(api_client)
        result = api_instance.zoek_haltes("centraal station")
        pprint(result)
print(perf_counter() - start)