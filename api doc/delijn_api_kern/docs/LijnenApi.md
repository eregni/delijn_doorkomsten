# delijn_api_kern.LijnenApi

All URIs are relative to *https://api.delijn.be/DLKernOpenData/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geef_dienstregeling_voor_lijnrichting**](LijnenApi.md#geef_dienstregeling_voor_lijnrichting) | **GET** /lijnen/{entiteitnummer}/{lijnnummer}/lijnrichtingen/{richting}/dienstregelingen | geef de dienstregeling voor de opgegeven lijnrichting
[**geef_doorkomst_voor_lijnrichting**](LijnenApi.md#geef_doorkomst_voor_lijnrichting) | **GET** /lijnen/{entiteitnummer}/{lijnnummer}/lijnrichtingen/{richting}/real-time | geef de real-time doorkomsten voor de opgegeven lijnrichting
[**geef_gemeenten_voor_lijn**](LijnenApi.md#geef_gemeenten_voor_lijn) | **GET** /lijnen/{entiteitnummer}/{lijnnummer}/gemeenten | geef de gemeenten die bediend worden voor de opgegeven lijn
[**geef_geplande_storingen_voor_lijnrichting**](LijnenApi.md#geef_geplande_storingen_voor_lijnrichting) | **GET** /lijnen/{entiteitnummer}/{lijnnummer}/lijnrichtingen/{richting}/omleidingen | geef de omleidingen voor de opgegeven lijnrichting
[**geef_geplande_storingen_voor_lijnrichtingen_lijst**](LijnenApi.md#geef_geplande_storingen_voor_lijnrichtingen_lijst) | **GET** /lijnen/lijst/{lijnrichtingsleutels}/omleidingen | geef de omleidingen voor de opgegeven lijst van lijnrichtingen
[**geef_haltes_voor_lijnrichting**](LijnenApi.md#geef_haltes_voor_lijnrichting) | **GET** /lijnen/{entiteitnummer}/{lijnnummer}/lijnrichtingen/{richting}/haltes | geef de haltes die de door opgegeven lijnrichting worden bediend
[**geef_lijn**](LijnenApi.md#geef_lijn) | **GET** /lijnen/{entiteitnummer}/{lijnnummer} | geef een lijn op basis van het opgegeven lijnnummer
[**geef_lijn_lijst**](LijnenApi.md#geef_lijn_lijst) | **GET** /lijnen/lijst/{lijnsleutels} | geef een lijst van lijnen op basis van een lijst van lijn sleutels
[**geef_lijnen**](LijnenApi.md#geef_lijnen) | **GET** /lijnen | geef alle lijnen
[**geef_lijnkleur**](LijnenApi.md#geef_lijnkleur) | **GET** /lijnen/{entiteitnummer}/{lijnnummer}/lijnkleuren | geef de lijnkleuren voor het opgegeven lijnnummer
[**geef_lijnkleur_lijst**](LijnenApi.md#geef_lijnkleur_lijst) | **GET** /lijnen/lijst/{lijnsleutels}/lijnkleuren | geef de lijnkleuren van lijnen op basis van een lijst van lijn sleutels
[**geef_lijnrichting**](LijnenApi.md#geef_lijnrichting) | **GET** /lijnen/{entiteitnummer}/{lijnnummer}/lijnrichtingen/{richting} | geef een lijnrichting voor de opgegeven lijnrichtingcode
[**geef_lijnrichtingen**](LijnenApi.md#geef_lijnrichtingen) | **GET** /lijnen/{entiteitnummer}/{lijnnummer}/lijnrichtingen | geef de lijnrichtingen voor het opgegeven lijnnummer
[**geef_lijnrichtingen_lijst**](LijnenApi.md#geef_lijnrichtingen_lijst) | **GET** /lijnen/lijst/{lijnsleutels}/lijnrichtingen | geef de lijnrichtingen van lijnen op basis van een lijst van lijn sleutels
[**geef_on_geplande_storingen_voor_lijnrichting**](LijnenApi.md#geef_on_geplande_storingen_voor_lijnrichting) | **GET** /lijnen/{entiteitnummer}/{lijnnummer}/lijnrichtingen/{richting}/storingen | geef de storingen voor de opgegeven lijnrichting
[**geef_on_geplande_storingen_voor_lijnrichtingen_lijst**](LijnenApi.md#geef_on_geplande_storingen_voor_lijnrichtingen_lijst) | **GET** /lijnen/lijst/{lijnrichtingsleutels}/storingen | geef de storingen voor de opgegeven lijst van lijnrichtingen
[**geef_rit_voor_lijnrichting**](LijnenApi.md#geef_rit_voor_lijnrichting) | **GET** /lijnen/{entiteitnummer}/{lijnnummer}/lijnrichtingen/{richting}/rit/{ritnummer} | geef rit(ten) voor de opgegeven lijnrichting


# **geef_dienstregeling_voor_lijnrichting**
> Ritten geef_dienstregeling_voor_lijnrichting(entiteitnummer, lijnnummer, richting)

geef de dienstregeling voor de opgegeven lijnrichting

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.ritten import Ritten
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit
    lijnnummer = 1 # int | Format - int32. nummer van de lijn
    richting = "HEEN" # str | richting van de lijn
    datum = "datum_example" # str | datum in formaat yyyy-MM-dd met als default waarde de huidige datum (optional)

    # example passing only required values which don't have defaults set
    try:
        # geef de dienstregeling voor de opgegeven lijnrichting
        api_response = api_instance.geef_dienstregeling_voor_lijnrichting(entiteitnummer, lijnnummer, richting)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_dienstregeling_voor_lijnrichting: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de dienstregeling voor de opgegeven lijnrichting
        api_response = api_instance.geef_dienstregeling_voor_lijnrichting(entiteitnummer, lijnnummer, richting, datum=datum)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_dienstregeling_voor_lijnrichting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |
 **lijnnummer** | **int**| Format - int32. nummer van de lijn |
 **richting** | **str**| richting van de lijn |
 **datum** | **str**| datum in formaat yyyy-MM-dd met als default waarde de huidige datum | [optional]

### Return type

[**Ritten**](Ritten.md)

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

# **geef_doorkomst_voor_lijnrichting**
> Ritten geef_doorkomst_voor_lijnrichting(entiteitnummer, lijnnummer, richting)

geef de real-time doorkomsten voor de opgegeven lijnrichting

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.ritten import Ritten
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit
    lijnnummer = 1 # int | Format - int32. nummer van de lijn
    richting = "HEEN" # str | richting van de lijn

    # example passing only required values which don't have defaults set
    try:
        # geef de real-time doorkomsten voor de opgegeven lijnrichting
        api_response = api_instance.geef_doorkomst_voor_lijnrichting(entiteitnummer, lijnnummer, richting)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_doorkomst_voor_lijnrichting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |
 **lijnnummer** | **int**| Format - int32. nummer van de lijn |
 **richting** | **str**| richting van de lijn |

### Return type

[**Ritten**](Ritten.md)

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

# **geef_gemeenten_voor_lijn**
> Gemeenten geef_gemeenten_voor_lijn(entiteitnummer, lijnnummer)

geef de gemeenten die bediend worden voor de opgegeven lijn

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.gemeenten import Gemeenten
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit
    lijnnummer = 1 # int | Format - int32. nummer van de lijn

    # example passing only required values which don't have defaults set
    try:
        # geef de gemeenten die bediend worden voor de opgegeven lijn
        api_response = api_instance.geef_gemeenten_voor_lijn(entiteitnummer, lijnnummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_gemeenten_voor_lijn: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |
 **lijnnummer** | **int**| Format - int32. nummer van de lijn |

### Return type

[**Gemeenten**](Gemeenten.md)

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

# **geef_geplande_storingen_voor_lijnrichting**
> Omleidingen geef_geplande_storingen_voor_lijnrichting(entiteitnummer, lijnnummer, richting)

geef de omleidingen voor de opgegeven lijnrichting

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.omleidingen import Omleidingen
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit
    lijnnummer = 1 # int | Format - int32. nummer van de lijn
    richting = "HEEN" # str | richting van de lijn
    datum = "datum_example" # str | datum in formaat yyyy-MM-dd met als default waarde de huidige datum (optional)

    # example passing only required values which don't have defaults set
    try:
        # geef de omleidingen voor de opgegeven lijnrichting
        api_response = api_instance.geef_geplande_storingen_voor_lijnrichting(entiteitnummer, lijnnummer, richting)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_geplande_storingen_voor_lijnrichting: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de omleidingen voor de opgegeven lijnrichting
        api_response = api_instance.geef_geplande_storingen_voor_lijnrichting(entiteitnummer, lijnnummer, richting, datum=datum)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_geplande_storingen_voor_lijnrichting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |
 **lijnnummer** | **int**| Format - int32. nummer van de lijn |
 **richting** | **str**| richting van de lijn |
 **datum** | **str**| datum in formaat yyyy-MM-dd met als default waarde de huidige datum | [optional]

### Return type

[**Omleidingen**](Omleidingen.md)

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

# **geef_geplande_storingen_voor_lijnrichtingen_lijst**
> Omleidingen geef_geplande_storingen_voor_lijnrichtingen_lijst(lijnrichtingsleutels)

geef de omleidingen voor de opgegeven lijst van lijnrichtingen

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.omleidingen import Omleidingen
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    lijnrichtingsleutels = "lijnrichtingsleutels_example" # str | lijst van lijnrichtingen (bv 1_500_HEEN_1_550_TERUG)
    datum = "datum_example" # str | datum in formaat yyyy-MM-dd met als default waarde de huidige datum (optional)

    # example passing only required values which don't have defaults set
    try:
        # geef de omleidingen voor de opgegeven lijst van lijnrichtingen
        api_response = api_instance.geef_geplande_storingen_voor_lijnrichtingen_lijst(lijnrichtingsleutels)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_geplande_storingen_voor_lijnrichtingen_lijst: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de omleidingen voor de opgegeven lijst van lijnrichtingen
        api_response = api_instance.geef_geplande_storingen_voor_lijnrichtingen_lijst(lijnrichtingsleutels, datum=datum)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_geplande_storingen_voor_lijnrichtingen_lijst: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lijnrichtingsleutels** | **str**| lijst van lijnrichtingen (bv 1_500_HEEN_1_550_TERUG) |
 **datum** | **str**| datum in formaat yyyy-MM-dd met als default waarde de huidige datum | [optional]

### Return type

[**Omleidingen**](Omleidingen.md)

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

# **geef_haltes_voor_lijnrichting**
> Haltes geef_haltes_voor_lijnrichting(entiteitnummer, lijnnummer, richting)

geef de haltes die de door opgegeven lijnrichting worden bediend

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.haltes import Haltes
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    entiteitnummer = 1 # int | Format - int32.
    lijnnummer = 1 # int | Format - int32.
    richting = "HEEN" # str | 

    # example passing only required values which don't have defaults set
    try:
        # geef de haltes die de door opgegeven lijnrichting worden bediend
        api_response = api_instance.geef_haltes_voor_lijnrichting(entiteitnummer, lijnnummer, richting)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_haltes_voor_lijnrichting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. |
 **lijnnummer** | **int**| Format - int32. |
 **richting** | **str**|  |

### Return type

[**Haltes**](Haltes.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_lijn**
> Lijn geef_lijn(entiteitnummer, lijnnummer)

geef een lijn op basis van het opgegeven lijnnummer

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.lijn import Lijn
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    entiteitnummer = 1 # int | Format - int32.
    lijnnummer = 1 # int | Format - int32.

    # example passing only required values which don't have defaults set
    try:
        # geef een lijn op basis van het opgegeven lijnnummer
        api_response = api_instance.geef_lijn(entiteitnummer, lijnnummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_lijn: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. |
 **lijnnummer** | **int**| Format - int32. |

### Return type

[**Lijn**](Lijn.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | request met succes afgehandeld |  -  |
**404** | lijn is niet gevonden |  -  |
**500** | service of achterliggende systemen niet beschikbaar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_lijn_lijst**
> Lijnen geef_lijn_lijst(lijnsleutels)

geef een lijst van lijnen op basis van een lijst van lijn sleutels

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.lijnen import Lijnen
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    lijnsleutels = "lijnsleutels_example" # str | lijst van lijn sleutels (bv 1_500_1_550)

    # example passing only required values which don't have defaults set
    try:
        # geef een lijst van lijnen op basis van een lijst van lijn sleutels
        api_response = api_instance.geef_lijn_lijst(lijnsleutels)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_lijn_lijst: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lijnsleutels** | **str**| lijst van lijn sleutels (bv 1_500_1_550) |

### Return type

[**Lijnen**](Lijnen.md)

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

# **geef_lijnen**
> Lijnen geef_lijnen()

geef alle lijnen

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.lijnen import Lijnen
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # geef alle lijnen
        api_response = api_instance.geef_lijnen()
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_lijnen: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Lijnen**](Lijnen.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_lijnkleur**
> LijnkleurCodes geef_lijnkleur(entiteitnummer, lijnnummer)

geef de lijnkleuren voor het opgegeven lijnnummer

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.lijnkleur_codes import LijnkleurCodes
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    entiteitnummer = 1 # int | Format - int32.
    lijnnummer = 1 # int | Format - int32.

    # example passing only required values which don't have defaults set
    try:
        # geef de lijnkleuren voor het opgegeven lijnnummer
        api_response = api_instance.geef_lijnkleur(entiteitnummer, lijnnummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_lijnkleur: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. |
 **lijnnummer** | **int**| Format - int32. |

### Return type

[**LijnkleurCodes**](LijnkleurCodes.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_lijnkleur_lijst**
> LijnkleurCodes geef_lijnkleur_lijst(lijnsleutels)

geef de lijnkleuren van lijnen op basis van een lijst van lijn sleutels

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.lijnkleur_codes import LijnkleurCodes
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    lijnsleutels = "lijnsleutels_example" # str | lijst van lijn sleutels (bv 1_500_1_550)

    # example passing only required values which don't have defaults set
    try:
        # geef de lijnkleuren van lijnen op basis van een lijst van lijn sleutels
        api_response = api_instance.geef_lijnkleur_lijst(lijnsleutels)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_lijnkleur_lijst: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lijnsleutels** | **str**| lijst van lijn sleutels (bv 1_500_1_550) |

### Return type

[**LijnkleurCodes**](LijnkleurCodes.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_lijnrichting**
> Lijnrichting geef_lijnrichting(entiteitnummer, lijnnummer, richting)

geef een lijnrichting voor de opgegeven lijnrichtingcode

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.lijnrichting import Lijnrichting
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    entiteitnummer = 1 # int | Format - int32.
    lijnnummer = 1 # int | Format - int32.
    richting = "HEEN" # str | 

    # example passing only required values which don't have defaults set
    try:
        # geef een lijnrichting voor de opgegeven lijnrichtingcode
        api_response = api_instance.geef_lijnrichting(entiteitnummer, lijnnummer, richting)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_lijnrichting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. |
 **lijnnummer** | **int**| Format - int32. |
 **richting** | **str**|  |

### Return type

[**Lijnrichting**](Lijnrichting.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_lijnrichtingen**
> Lijnrichtingen geef_lijnrichtingen(entiteitnummer, lijnnummer)

geef de lijnrichtingen voor het opgegeven lijnnummer

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.lijnrichtingen import Lijnrichtingen
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    entiteitnummer = 1 # int | Format - int32.
    lijnnummer = 1 # int | Format - int32.

    # example passing only required values which don't have defaults set
    try:
        # geef de lijnrichtingen voor het opgegeven lijnnummer
        api_response = api_instance.geef_lijnrichtingen(entiteitnummer, lijnnummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_lijnrichtingen: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. |
 **lijnnummer** | **int**| Format - int32. |

### Return type

[**Lijnrichtingen**](Lijnrichtingen.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_lijnrichtingen_lijst**
> LijnLijnrichtingenLijst geef_lijnrichtingen_lijst(lijnsleutels)

geef de lijnrichtingen van lijnen op basis van een lijst van lijn sleutels

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.lijn_lijnrichtingen_lijst import LijnLijnrichtingenLijst
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    lijnsleutels = "lijnsleutels_example" # str | lijst van lijn sleutels (bv 1_500_1_550)

    # example passing only required values which don't have defaults set
    try:
        # geef de lijnrichtingen van lijnen op basis van een lijst van lijn sleutels
        api_response = api_instance.geef_lijnrichtingen_lijst(lijnsleutels)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_lijnrichtingen_lijst: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lijnsleutels** | **str**| lijst van lijn sleutels (bv 1_500_1_550) |

### Return type

[**LijnLijnrichtingenLijst**](LijnLijnrichtingenLijst.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_on_geplande_storingen_voor_lijnrichting**
> Omleidingen geef_on_geplande_storingen_voor_lijnrichting(entiteitnummer, lijnnummer, richting)

geef de storingen voor de opgegeven lijnrichting

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.omleidingen import Omleidingen
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit
    lijnnummer = 1 # int | Format - int32. nummer van de lijn
    richting = "HEEN" # str | richting van de lijn
    datum = "datum_example" # str | datum in formaat yyyy-MM-dd met als default waarde de huidige datum (optional)

    # example passing only required values which don't have defaults set
    try:
        # geef de storingen voor de opgegeven lijnrichting
        api_response = api_instance.geef_on_geplande_storingen_voor_lijnrichting(entiteitnummer, lijnnummer, richting)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_on_geplande_storingen_voor_lijnrichting: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de storingen voor de opgegeven lijnrichting
        api_response = api_instance.geef_on_geplande_storingen_voor_lijnrichting(entiteitnummer, lijnnummer, richting, datum=datum)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_on_geplande_storingen_voor_lijnrichting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |
 **lijnnummer** | **int**| Format - int32. nummer van de lijn |
 **richting** | **str**| richting van de lijn |
 **datum** | **str**| datum in formaat yyyy-MM-dd met als default waarde de huidige datum | [optional]

### Return type

[**Omleidingen**](Omleidingen.md)

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

# **geef_on_geplande_storingen_voor_lijnrichtingen_lijst**
> Omleidingen geef_on_geplande_storingen_voor_lijnrichtingen_lijst(lijnrichtingsleutels)

geef de storingen voor de opgegeven lijst van lijnrichtingen

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.omleidingen import Omleidingen
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    lijnrichtingsleutels = "lijnrichtingsleutels_example" # str | lijst van lijnrichtingen (bv 1_500_HEEN_1_550_TERUG)
    datum = "datum_example" # str | datum in formaat yyyy-MM-dd met als default waarde de huidige datum (optional)

    # example passing only required values which don't have defaults set
    try:
        # geef de storingen voor de opgegeven lijst van lijnrichtingen
        api_response = api_instance.geef_on_geplande_storingen_voor_lijnrichtingen_lijst(lijnrichtingsleutels)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_on_geplande_storingen_voor_lijnrichtingen_lijst: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de storingen voor de opgegeven lijst van lijnrichtingen
        api_response = api_instance.geef_on_geplande_storingen_voor_lijnrichtingen_lijst(lijnrichtingsleutels, datum=datum)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_on_geplande_storingen_voor_lijnrichtingen_lijst: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lijnrichtingsleutels** | **str**| lijst van lijnrichtingen (bv 1_500_HEEN_1_550_TERUG) |
 **datum** | **str**| datum in formaat yyyy-MM-dd met als default waarde de huidige datum | [optional]

### Return type

[**Omleidingen**](Omleidingen.md)

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

# **geef_rit_voor_lijnrichting**
> Ritten geef_rit_voor_lijnrichting(entiteitnummer, lijnnummer, richting, ritnummer)

geef rit(ten) voor de opgegeven lijnrichting

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import lijnen_api
from delijn_api_kern.model.ritten import Ritten
from pprint import pprint
# Defining the host is optional and defaults to https://api.delijn.be/DLKernOpenData/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = delijn_api_kern.Configuration(
    host = "https://api.delijn.be/DLKernOpenData/api/v1"
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
with delijn_api_kern.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lijnen_api.LijnenApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit
    lijnnummer = 1 # int | Format - int32. nummer van de lijn
    richting = "HEEN" # str | richting van de lijn
    ritnummer = "ritnummer_example" # str | nummer van de rit
    datum = "datum_example" # str | exploitatie datum in formaat yyyy-MM-dd met huidige datum als default (optional)

    # example passing only required values which don't have defaults set
    try:
        # geef rit(ten) voor de opgegeven lijnrichting
        api_response = api_instance.geef_rit_voor_lijnrichting(entiteitnummer, lijnnummer, richting, ritnummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_rit_voor_lijnrichting: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef rit(ten) voor de opgegeven lijnrichting
        api_response = api_instance.geef_rit_voor_lijnrichting(entiteitnummer, lijnnummer, richting, ritnummer, datum=datum)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling LijnenApi->geef_rit_voor_lijnrichting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |
 **lijnnummer** | **int**| Format - int32. nummer van de lijn |
 **richting** | **str**| richting van de lijn |
 **ritnummer** | **str**| nummer van de rit |
 **datum** | **str**| exploitatie datum in formaat yyyy-MM-dd met huidige datum als default | [optional]

### Return type

[**Ritten**](Ritten.md)

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

