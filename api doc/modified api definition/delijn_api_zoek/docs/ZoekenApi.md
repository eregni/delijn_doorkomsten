# delijn_api_zoek.ZoekenApi

All URIs are relative to *https://api.delijn.be/DLZoekOpenData/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zoek_haltes**](ZoekenApi.md#zoek_haltes) | **GET** /zoek/haltes/{zoekArgument} | zoekHaltes
[**zoek_lijnrichtingen**](ZoekenApi.md#zoek_lijnrichtingen) | **GET** /zoek/lijnrichtingen/{zoekArgument} | zoekLijnrichtingen
[**zoek_locaties**](ZoekenApi.md#zoek_locaties) | **GET** /zoek/locaties/{zoekArgument} | zoekLocaties


# **zoek_haltes**
> HaltesHits zoek_haltes(zoek_argument)

zoekHaltes

zoekHaltes

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_zoek
from delijn_api_zoek.api import zoeken_api
from delijn_api_zoek.model.haltes_hits import HaltesHits
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLZoekOpenData/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_zoek.Configuration(
    host = "https://api.delijn.be/DLZoekOpenData/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Configure API key authorization: apiKeyQuery
configuration.api_key['apiKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyQuery'] = 'Bearer'

# Enter a context with an instance of the API client
with delijn_api_zoek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zoeken_api.ZoekenApi(api_client)
    zoek_argument = "zoekArgument_example" # str | het zoekargument
    huidige_positie = "huidigePositie_example" # str | de latitude en longitude coordinaat waarden gescheiden door komma bv, 51.056064,3.797336 van de lokatie waarvoor haltes in de buurt gezocht wordt (optional)
    start_index = 0 # int | Format - int32. de start positie in de lijst van gevonden haltes (optional) if omitted the server will use the default value of 0
    max_aantal_hits = 10 # int | Format - int32. het maximaal aantal haltes aangeleverd door deze service  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # zoekHaltes
        api_response = api_instance.zoek_haltes(zoek_argument)
        pprint(api_response)
    except delijn_api_zoek.ApiException as e:
        print("Exception when calling ZoekenApi->zoek_haltes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # zoekHaltes
        api_response = api_instance.zoek_haltes(zoek_argument, huidige_positie=huidige_positie, start_index=start_index, max_aantal_hits=max_aantal_hits)
        pprint(api_response)
    except delijn_api_zoek.ApiException as e:
        print("Exception when calling ZoekenApi->zoek_haltes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zoek_argument** | **str**| het zoekargument |
 **huidige_positie** | **str**| de latitude en longitude coordinaat waarden gescheiden door komma bv, 51.056064,3.797336 van de lokatie waarvoor haltes in de buurt gezocht wordt | [optional]
 **start_index** | **int**| Format - int32. de start positie in de lijst van gevonden haltes | [optional] if omitted the server will use the default value of 0
 **max_aantal_hits** | **int**| Format - int32. het maximaal aantal haltes aangeleverd door deze service  | [optional] if omitted the server will use the default value of 10

### Return type

[**HaltesHits**](HaltesHits.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**500** | service of achterliggende systemen niet beschikbaar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zoek_lijnrichtingen**
> LijnRichtingHits zoek_lijnrichtingen(zoek_argument)

zoekLijnrichtingen

zoekLijnrichtingen

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_zoek
from delijn_api_zoek.api import zoeken_api
from delijn_api_zoek.model.lijn_richting_hits import LijnRichtingHits
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLZoekOpenData/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_zoek.Configuration(
    host = "https://api.delijn.be/DLZoekOpenData/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Configure API key authorization: apiKeyQuery
configuration.api_key['apiKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyQuery'] = 'Bearer'

# Enter a context with an instance of the API client
with delijn_api_zoek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zoeken_api.ZoekenApi(api_client)
    zoek_argument = "zoekArgument_example" # str | het zoekargument
    huidige_positie = "huidigePositie_example" # str | de latitude en longitude coordinaat waarden gescheiden door komma bv, 51.056064,3.797336 van de lokatie waarvoor lijnen in de buurt gezocht wordt (optional)
    start_index = 0 # int | Format - int32. de start positie in de lijst van gevonden lijnen (optional) if omitted the server will use the default value of 0
    max_aantal_hits = 10 # int | Format - int32. het maximaal aantal lijnen aangeleverd door deze service  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # zoekLijnrichtingen
        api_response = api_instance.zoek_lijnrichtingen(zoek_argument)
        pprint(api_response)
    except delijn_api_zoek.ApiException as e:
        print("Exception when calling ZoekenApi->zoek_lijnrichtingen: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # zoekLijnrichtingen
        api_response = api_instance.zoek_lijnrichtingen(zoek_argument, huidige_positie=huidige_positie, start_index=start_index, max_aantal_hits=max_aantal_hits)
        pprint(api_response)
    except delijn_api_zoek.ApiException as e:
        print("Exception when calling ZoekenApi->zoek_lijnrichtingen: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zoek_argument** | **str**| het zoekargument |
 **huidige_positie** | **str**| de latitude en longitude coordinaat waarden gescheiden door komma bv, 51.056064,3.797336 van de lokatie waarvoor lijnen in de buurt gezocht wordt | [optional]
 **start_index** | **int**| Format - int32. de start positie in de lijst van gevonden lijnen | [optional] if omitted the server will use the default value of 0
 **max_aantal_hits** | **int**| Format - int32. het maximaal aantal lijnen aangeleverd door deze service  | [optional] if omitted the server will use the default value of 10

### Return type

[**LijnRichtingHits**](LijnRichtingHits.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**500** | service of achterliggende systemen niet beschikbaar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zoek_locaties**
> LocatiesHits zoek_locaties(zoek_argument)

zoekLocaties

zoekLocaties

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_zoek
from delijn_api_zoek.api import zoeken_api
from delijn_api_zoek.model.locaties_hits import LocatiesHits
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLZoekOpenData/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_zoek.Configuration(
    host = "https://api.delijn.be/DLZoekOpenData/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Configure API key authorization: apiKeyQuery
configuration.api_key['apiKeyQuery'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyQuery'] = 'Bearer'

# Enter a context with an instance of the API client
with delijn_api_zoek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zoeken_api.ZoekenApi(api_client)
    zoek_argument = "zoekArgument_example" # str | het zoekargument
    huidige_positie = "huidigePositie_example" # str | momenteel niet ondersteund voor lokaties (optional)
    start_index = 0 # int | Format - int32. de start positie in de lijst van gevonden lokaties (optional) if omitted the server will use the default value of 0
    max_aantal_hits = 10 # int | Format - int32. het maximaal aantal lokaties aangeleverd door deze service  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # zoekLocaties
        api_response = api_instance.zoek_locaties(zoek_argument)
        pprint(api_response)
    except delijn_api_zoek.ApiException as e:
        print("Exception when calling ZoekenApi->zoek_locaties: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # zoekLocaties
        api_response = api_instance.zoek_locaties(zoek_argument, huidige_positie=huidige_positie, start_index=start_index, max_aantal_hits=max_aantal_hits)
        pprint(api_response)
    except delijn_api_zoek.ApiException as e:
        print("Exception when calling ZoekenApi->zoek_locaties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zoek_argument** | **str**| het zoekargument |
 **huidige_positie** | **str**| momenteel niet ondersteund voor lokaties | [optional]
 **start_index** | **int**| Format - int32. de start positie in de lijst van gevonden lokaties | [optional] if omitted the server will use the default value of 0
 **max_aantal_hits** | **int**| Format - int32. het maximaal aantal lokaties aangeleverd door deze service  | [optional] if omitted the server will use the default value of 10

### Return type

[**LocatiesHits**](LocatiesHits.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**500** | service of achterliggende systemen niet beschikbaar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

