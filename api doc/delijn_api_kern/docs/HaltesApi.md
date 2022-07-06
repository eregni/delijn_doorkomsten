# delijn_api_kern.HaltesApi

All URIs are relative to *https://api.delijn.be/DLKernOpenData/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geef_dienstregeling_voor_halte**](HaltesApi.md#geef_dienstregeling_voor_halte) | **GET** /haltes/{entiteitnummer}/{haltenummer}/dienstregelingen | geef de dienstregeling voor de opgegeven halte
[**geef_dienstregeling_voor_halte_lijst**](HaltesApi.md#geef_dienstregeling_voor_halte_lijst) | **GET** /haltes/lijst/{haltesleutels}/dienstregelingen | geef de dienstregeling voor de opgegeven halte sleutels
[**geef_doorkomsten_voor_halte**](HaltesApi.md#geef_doorkomsten_voor_halte) | **GET** /haltes/{entiteitnummer}/{haltenummer}/real-time | geef de real-time doorkomsten voor de opgegeven halte
[**geef_doorkomsten_voor_halte_lijst**](HaltesApi.md#geef_doorkomsten_voor_halte_lijst) | **GET** /haltes/lijst/{haltesleutels}/real-time | geef de real-time doorkomsten voor de opgegeven halte sleutels
[**geef_halte**](HaltesApi.md#geef_halte) | **GET** /haltes/{entiteitnummer}/{haltenummer} | geef een halte op basis van het opgegeven haltenummer
[**geef_halte_lijnrichtingen_lijst**](HaltesApi.md#geef_halte_lijnrichtingen_lijst) | **GET** /haltes/lijst/{haltesleutels}/lijnrichtingen | geef de lijnrichtingen die de opgegeven halte bedienen op basis van een lijst van halte sleutels
[**geef_halte_lijst**](HaltesApi.md#geef_halte_lijst) | **GET** /haltes/lijst/{haltesleutels} | geef een lijst van haltes op basis van een lijst van halte sleutels
[**geef_haltes**](HaltesApi.md#geef_haltes) | **GET** /haltes | geef alle haltes
[**geef_haltes_indebuurt**](HaltesApi.md#geef_haltes_indebuurt) | **GET** /haltes/indebuurt/{latlng} | geef de haltes van de verschillende vervoersmaatschappijen in de buurt van de opgegeven coordinaten
[**geef_lijnrichtingen_voor_halte**](HaltesApi.md#geef_lijnrichtingen_voor_halte) | **GET** /haltes/{entiteitnummer}/{haltenummer}/lijnrichtingen | geef de lijnrichtingen die de opgegeven halte bedienen
[**geef_omleidingen_voor_halte**](HaltesApi.md#geef_omleidingen_voor_halte) | **GET** /haltes/{entiteitnummer}/{haltenummer}/omleidingen | geef de omleidingen voor de opgegeven halte
[**geef_omleidingen_voor_halte_lijst**](HaltesApi.md#geef_omleidingen_voor_halte_lijst) | **GET** /haltes/lijst/{haltesleutels}/omleidingen | geef de omleidingen voor de opgegeven halte sleutels
[**geef_storingen_voor_halte**](HaltesApi.md#geef_storingen_voor_halte) | **GET** /haltes/{entiteitnummer}/{haltenummer}/storingen | geef de storingen voor de opgegeven halte
[**geef_storingen_voor_halte_lijst**](HaltesApi.md#geef_storingen_voor_halte_lijst) | **GET** /haltes/lijst/{haltesleutels}/storingen | geef de storingen de opgegeven halte sleutels


# **geef_dienstregeling_voor_halte**
> Ritten geef_dienstregeling_voor_halte(entiteitnummer, haltenummer)

geef de dienstregeling voor de opgegeven halte

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import haltes_api
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
    api_instance = haltes_api.HaltesApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit
    haltenummer = 1 # int | Format - int32. nummer van de halte
    datum = "datum_example" # str | datum in formaat yyyy-MM-dd met als default waarde de huidige datum (optional)
    inclusief_ritnummer = True # bool | het ritnummer is gewenst in het resultaat (performance impact) (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # geef de dienstregeling voor de opgegeven halte
        api_response = api_instance.geef_dienstregeling_voor_halte(entiteitnummer, haltenummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_dienstregeling_voor_halte: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de dienstregeling voor de opgegeven halte
        api_response = api_instance.geef_dienstregeling_voor_halte(entiteitnummer, haltenummer, datum=datum, inclusief_ritnummer=inclusief_ritnummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_dienstregeling_voor_halte: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |
 **haltenummer** | **int**| Format - int32. nummer van de halte |
 **datum** | **str**| datum in formaat yyyy-MM-dd met als default waarde de huidige datum | [optional]
 **inclusief_ritnummer** | **bool**| het ritnummer is gewenst in het resultaat (performance impact) | [optional] if omitted the server will use the default value of True

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

# **geef_dienstregeling_voor_halte_lijst**
> HalteDoorkomstenLijst geef_dienstregeling_voor_halte_lijst(haltesleutels)

geef de dienstregeling voor de opgegeven halte sleutels

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import haltes_api
from delijn_api_kern.model.halte_doorkomsten_lijst import HalteDoorkomstenLijst
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
    api_instance = haltes_api.HaltesApi(api_client)
    haltesleutels = "haltesleutels_example" # str | lijst van halte sleutels (bv 1_201302_5_5024541)
    datum = "datum_example" # str | datum in formaat yyyy-MM-dd met als default waarde de huidige datum (optional)
    inclusief_ritnummer = True # bool | het ritnummer is gewenst in het resultaat (performance impact) (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # geef de dienstregeling voor de opgegeven halte sleutels
        api_response = api_instance.geef_dienstregeling_voor_halte_lijst(haltesleutels)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_dienstregeling_voor_halte_lijst: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de dienstregeling voor de opgegeven halte sleutels
        api_response = api_instance.geef_dienstregeling_voor_halte_lijst(haltesleutels, datum=datum, inclusief_ritnummer=inclusief_ritnummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_dienstregeling_voor_halte_lijst: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haltesleutels** | **str**| lijst van halte sleutels (bv 1_201302_5_5024541) |
 **datum** | **str**| datum in formaat yyyy-MM-dd met als default waarde de huidige datum | [optional]
 **inclusief_ritnummer** | **bool**| het ritnummer is gewenst in het resultaat (performance impact) | [optional] if omitted the server will use the default value of True

### Return type

[**HalteDoorkomstenLijst**](HalteDoorkomstenLijst.md)

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

# **geef_doorkomsten_voor_halte**
> Ritten geef_doorkomsten_voor_halte(entiteitnummer, haltenummer)

geef de real-time doorkomsten voor de opgegeven halte

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import haltes_api
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
    api_instance = haltes_api.HaltesApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit
    haltenummer = 1 # int | Format - int32. nummer van de halte
    max_aantal_doorkomsten = 10 # int | Format - int32. maximaal aantal doorkomsten voor de opgegeven halte (optional) if omitted the server will use the default value of 10
    ocp_apim_subscription_key = "Ocp-Apim-Subscription-Key_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # geef de real-time doorkomsten voor de opgegeven halte
        api_response = api_instance.geef_doorkomsten_voor_halte(entiteitnummer, haltenummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_doorkomsten_voor_halte: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de real-time doorkomsten voor de opgegeven halte
        api_response = api_instance.geef_doorkomsten_voor_halte(entiteitnummer, haltenummer, max_aantal_doorkomsten=max_aantal_doorkomsten, ocp_apim_subscription_key=ocp_apim_subscription_key)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_doorkomsten_voor_halte: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |
 **haltenummer** | **int**| Format - int32. nummer van de halte |
 **max_aantal_doorkomsten** | **int**| Format - int32. maximaal aantal doorkomsten voor de opgegeven halte | [optional] if omitted the server will use the default value of 10
 **ocp_apim_subscription_key** | **str**|  | [optional]

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

# **geef_doorkomsten_voor_halte_lijst**
> HalteDoorkomstenLijst geef_doorkomsten_voor_halte_lijst(haltesleutels)

geef de real-time doorkomsten voor de opgegeven halte sleutels

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import haltes_api
from delijn_api_kern.model.halte_doorkomsten_lijst import HalteDoorkomstenLijst
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
    api_instance = haltes_api.HaltesApi(api_client)
    haltesleutels = "haltesleutels_example" # str | lijst van halte sleutels (bv 1_201302_5_5024541)
    max_aantal_doorkomsten = 10 # int | Format - int32. maximaal aantal doorkomsten voor de opgegeven halte (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # geef de real-time doorkomsten voor de opgegeven halte sleutels
        api_response = api_instance.geef_doorkomsten_voor_halte_lijst(haltesleutels)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_doorkomsten_voor_halte_lijst: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de real-time doorkomsten voor de opgegeven halte sleutels
        api_response = api_instance.geef_doorkomsten_voor_halte_lijst(haltesleutels, max_aantal_doorkomsten=max_aantal_doorkomsten)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_doorkomsten_voor_halte_lijst: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haltesleutels** | **str**| lijst van halte sleutels (bv 1_201302_5_5024541) |
 **max_aantal_doorkomsten** | **int**| Format - int32. maximaal aantal doorkomsten voor de opgegeven halte | [optional] if omitted the server will use the default value of 10

### Return type

[**HalteDoorkomstenLijst**](HalteDoorkomstenLijst.md)

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

# **geef_halte**
> Halte geef_halte(entiteitnummer, haltenummer)

geef een halte op basis van het opgegeven haltenummer

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import haltes_api
from delijn_api_kern.model.halte import Halte
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
    api_instance = haltes_api.HaltesApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit
    haltenummer = 1 # int | Format - int32. nummer van de entiteit

    # example passing only required values which don't have defaults set
    try:
        # geef een halte op basis van het opgegeven haltenummer
        api_response = api_instance.geef_halte(entiteitnummer, haltenummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_halte: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |
 **haltenummer** | **int**| Format - int32. nummer van de entiteit |

### Return type

[**Halte**](Halte.md)

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

# **geef_halte_lijnrichtingen_lijst**
> Lijnrichtingen geef_halte_lijnrichtingen_lijst(haltesleutels)

geef de lijnrichtingen die de opgegeven halte bedienen op basis van een lijst van halte sleutels

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import haltes_api
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
    api_instance = haltes_api.HaltesApi(api_client)
    haltesleutels = "haltesleutels_example" # str | lijst van halte sleutels (bv 1_201302_5_5024541)

    # example passing only required values which don't have defaults set
    try:
        # geef de lijnrichtingen die de opgegeven halte bedienen op basis van een lijst van halte sleutels
        api_response = api_instance.geef_halte_lijnrichtingen_lijst(haltesleutels)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_halte_lijnrichtingen_lijst: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haltesleutels** | **str**| lijst van halte sleutels (bv 1_201302_5_5024541) |

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
**500** | service of achterliggende systemen niet beschikbaar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_halte_lijst**
> Haltes geef_halte_lijst(haltesleutels)

geef een lijst van haltes op basis van een lijst van halte sleutels

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import haltes_api
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
    api_instance = haltes_api.HaltesApi(api_client)
    haltesleutels = "haltesleutels_example" # str | lijst van halte sleutels (bv 1_201302_5_5024541)

    # example passing only required values which don't have defaults set
    try:
        # geef een lijst van haltes op basis van een lijst van halte sleutels
        api_response = api_instance.geef_halte_lijst(haltesleutels)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_halte_lijst: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haltesleutels** | **str**| lijst van halte sleutels (bv 1_201302_5_5024541) |

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
**400** | ongeldige waarden als input |  -  |
**500** | service of achterliggende systemen niet beschikbaar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_haltes**
> Haltes geef_haltes()

geef alle haltes

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import haltes_api
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
    api_instance = haltes_api.HaltesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # geef alle haltes
        api_response = api_instance.geef_haltes()
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_haltes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**500** | service of achterliggende systemen niet beschikbaar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_haltes_indebuurt**
> Punten geef_haltes_indebuurt(latlng)

geef de haltes van de verschillende vervoersmaatschappijen in de buurt van de opgegeven coordinaten

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import haltes_api
from delijn_api_kern.model.punten import Punten
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
    api_instance = haltes_api.HaltesApi(api_client)
    latlng = "latlng_example" # str | latitude en longitude gescheiden door komma bv, 51.056064,3.797336
    radius = 750 # int | Format - int32. de radius in meters binnen de welke naar haltes gezocht wordt (optional) if omitted the server will use the default value of 750
    max_aantal_haltes = 999 # int | Format - int32. het maximaal aantal haltes die van de operatie verwacht wordt (optional) if omitted the server will use the default value of 999

    # example passing only required values which don't have defaults set
    try:
        # geef de haltes van de verschillende vervoersmaatschappijen in de buurt van de opgegeven coordinaten
        api_response = api_instance.geef_haltes_indebuurt(latlng)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_haltes_indebuurt: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de haltes van de verschillende vervoersmaatschappijen in de buurt van de opgegeven coordinaten
        api_response = api_instance.geef_haltes_indebuurt(latlng, radius=radius, max_aantal_haltes=max_aantal_haltes)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_haltes_indebuurt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latlng** | **str**| latitude en longitude gescheiden door komma bv, 51.056064,3.797336 |
 **radius** | **int**| Format - int32. de radius in meters binnen de welke naar haltes gezocht wordt | [optional] if omitted the server will use the default value of 750
 **max_aantal_haltes** | **int**| Format - int32. het maximaal aantal haltes die van de operatie verwacht wordt | [optional] if omitted the server will use the default value of 999

### Return type

[**Punten**](Punten.md)

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

# **geef_lijnrichtingen_voor_halte**
> Lijnrichtingen geef_lijnrichtingen_voor_halte(entiteitnummer, haltenummer)

geef de lijnrichtingen die de opgegeven halte bedienen

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import haltes_api
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
    api_instance = haltes_api.HaltesApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit
    haltenummer = 1 # int | Format - int32. nummer van de halte

    # example passing only required values which don't have defaults set
    try:
        # geef de lijnrichtingen die de opgegeven halte bedienen
        api_response = api_instance.geef_lijnrichtingen_voor_halte(entiteitnummer, haltenummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_lijnrichtingen_voor_halte: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |
 **haltenummer** | **int**| Format - int32. nummer van de halte |

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
**500** | service of achterliggende systemen niet beschikbaar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_omleidingen_voor_halte**
> Omleidingen geef_omleidingen_voor_halte(entiteitnummer, haltenummer)

geef de omleidingen voor de opgegeven halte

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import haltes_api
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
    api_instance = haltes_api.HaltesApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit
    haltenummer = 1 # int | Format - int32. nummer van de halte
    datum = "datum_example" # str | datum in formaat yyyy-MM-dd met als default waarde de huidige datum (optional)

    # example passing only required values which don't have defaults set
    try:
        # geef de omleidingen voor de opgegeven halte
        api_response = api_instance.geef_omleidingen_voor_halte(entiteitnummer, haltenummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_omleidingen_voor_halte: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de omleidingen voor de opgegeven halte
        api_response = api_instance.geef_omleidingen_voor_halte(entiteitnummer, haltenummer, datum=datum)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_omleidingen_voor_halte: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |
 **haltenummer** | **int**| Format - int32. nummer van de halte |
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

# **geef_omleidingen_voor_halte_lijst**
> HalteOmleidingenLijst geef_omleidingen_voor_halte_lijst(haltesleutels)

geef de omleidingen voor de opgegeven halte sleutels

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import haltes_api
from delijn_api_kern.model.halte_omleidingen_lijst import HalteOmleidingenLijst
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
    api_instance = haltes_api.HaltesApi(api_client)
    haltesleutels = "haltesleutels_example" # str | lijst van halte sleutels (bv 1_201302_5_5024541)
    datum = "datum_example" # str | datum in formaat yyyy-MM-dd met als default waarde de huidige datum (optional)

    # example passing only required values which don't have defaults set
    try:
        # geef de omleidingen voor de opgegeven halte sleutels
        api_response = api_instance.geef_omleidingen_voor_halte_lijst(haltesleutels)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_omleidingen_voor_halte_lijst: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de omleidingen voor de opgegeven halte sleutels
        api_response = api_instance.geef_omleidingen_voor_halte_lijst(haltesleutels, datum=datum)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_omleidingen_voor_halte_lijst: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haltesleutels** | **str**| lijst van halte sleutels (bv 1_201302_5_5024541) |
 **datum** | **str**| datum in formaat yyyy-MM-dd met als default waarde de huidige datum | [optional]

### Return type

[**HalteOmleidingenLijst**](HalteOmleidingenLijst.md)

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

# **geef_storingen_voor_halte**
> Omleidingen geef_storingen_voor_halte(entiteitnummer, haltenummer)

geef de storingen voor de opgegeven halte

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import haltes_api
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
    api_instance = haltes_api.HaltesApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit
    haltenummer = 1 # int | Format - int32. nummer van de halte
    datum = "datum_example" # str | datum in formaat yyyy-MM-dd met als default waarde de huidige datum (optional)

    # example passing only required values which don't have defaults set
    try:
        # geef de storingen voor de opgegeven halte
        api_response = api_instance.geef_storingen_voor_halte(entiteitnummer, haltenummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_storingen_voor_halte: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de storingen voor de opgegeven halte
        api_response = api_instance.geef_storingen_voor_halte(entiteitnummer, haltenummer, datum=datum)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_storingen_voor_halte: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |
 **haltenummer** | **int**| Format - int32. nummer van de halte |
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
**404** | omleiding is niet gevonden |  -  |
**500** | service of achterliggende systemen niet beschikbaar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_storingen_voor_halte_lijst**
> Omleidingen geef_storingen_voor_halte_lijst(haltesleutels)

geef de storingen de opgegeven halte sleutels

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import haltes_api
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
    api_instance = haltes_api.HaltesApi(api_client)
    haltesleutels = "haltesleutels_example" # str | lijst van halte sleutels (bv 1_201302_5_5024541)
    datum = "datum_example" # str | datum in formaat yyyy-MM-dd met als default waarde de huidige datum (optional)

    # example passing only required values which don't have defaults set
    try:
        # geef de storingen de opgegeven halte sleutels
        api_response = api_instance.geef_storingen_voor_halte_lijst(haltesleutels)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_storingen_voor_halte_lijst: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de storingen de opgegeven halte sleutels
        api_response = api_instance.geef_storingen_voor_halte_lijst(haltesleutels, datum=datum)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling HaltesApi->geef_storingen_voor_halte_lijst: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haltesleutels** | **str**| lijst van halte sleutels (bv 1_201302_5_5024541) |
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

