# delijn_api_kern.GemeentenApi

All URIs are relative to *https://api.delijn.be/DLKernOpenData/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geef_gemeente**](GemeentenApi.md#geef_gemeente) | **GET** /gemeenten/{gemeenteNummer} | geef een gemeente op basis van het opgegeven gemeentenummer
[**geef_gemeenten**](GemeentenApi.md#geef_gemeenten) | **GET** /gemeenten | geef alle gemeenten
[**geef_haltes_voor_gemeente**](GemeentenApi.md#geef_haltes_voor_gemeente) | **GET** /gemeenten/{gemeenteNummer}/haltes | geef alle haltes binnen een gemeente
[**geef_haltes_voor_gemeentes**](GemeentenApi.md#geef_haltes_voor_gemeentes) | **GET** /gemeenten/lijst/{gemeenteNummers}/haltes | geef alle haltes voor de lijst van gemeentenummers
[**geef_lijnen_voor_gemeente**](GemeentenApi.md#geef_lijnen_voor_gemeente) | **GET** /gemeenten/{gemeenteNummer}/lijnen | geef alle lijnen die een gemeente bedienen


# **geef_gemeente**
> Gemeente geef_gemeente(gemeente_nummer)

geef een gemeente op basis van het opgegeven gemeentenummer

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import gemeenten_api
from delijn_api_kern.model.gemeente import Gemeente
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
    api_instance = gemeenten_api.GemeentenApi(api_client)
    gemeente_nummer = 1 # int | Format - int32. nummer van de gemeente

    # example passing only required values which don't have defaults set
    try:
        # geef een gemeente op basis van het opgegeven gemeentenummer
        api_response = api_instance.geef_gemeente(gemeente_nummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling GemeentenApi->geef_gemeente: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gemeente_nummer** | **int**| Format - int32. nummer van de gemeente |

### Return type

[**Gemeente**](Gemeente.md)

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

# **geef_gemeenten**
> Gemeenten geef_gemeenten()

geef alle gemeenten

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import gemeenten_api
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
    api_instance = gemeenten_api.GemeentenApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # geef alle gemeenten
        api_response = api_instance.geef_gemeenten()
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling GemeentenApi->geef_gemeenten: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Gemeenten**](Gemeenten.md)

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

# **geef_haltes_voor_gemeente**
> Haltes geef_haltes_voor_gemeente(gemeente_nummer)

geef alle haltes binnen een gemeente

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import gemeenten_api
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
    api_instance = gemeenten_api.GemeentenApi(api_client)
    gemeente_nummer = 1 # int | Format - int32. nummer van de gemeente

    # example passing only required values which don't have defaults set
    try:
        # geef alle haltes binnen een gemeente
        api_response = api_instance.geef_haltes_voor_gemeente(gemeente_nummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling GemeentenApi->geef_haltes_voor_gemeente: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gemeente_nummer** | **int**| Format - int32. nummer van de gemeente |

### Return type

[**Haltes**](Haltes.md)

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

# **geef_haltes_voor_gemeentes**
> Haltes geef_haltes_voor_gemeentes(gemeente_nummers)

geef alle haltes voor de lijst van gemeentenummers

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import gemeenten_api
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
    api_instance = gemeenten_api.GemeentenApi(api_client)
    gemeente_nummers = "gemeenteNummers_example" # str | nummers van de gemeente

    # example passing only required values which don't have defaults set
    try:
        # geef alle haltes voor de lijst van gemeentenummers
        api_response = api_instance.geef_haltes_voor_gemeentes(gemeente_nummers)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling GemeentenApi->geef_haltes_voor_gemeentes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gemeente_nummers** | **str**| nummers van de gemeente |

### Return type

[**Haltes**](Haltes.md)

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

# **geef_lijnen_voor_gemeente**
> Lijnen geef_lijnen_voor_gemeente(gemeente_nummer)

geef alle lijnen die een gemeente bedienen

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import gemeenten_api
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
    api_instance = gemeenten_api.GemeentenApi(api_client)
    gemeente_nummer = 1 # int | Format - int32. nummer van de gemeente

    # example passing only required values which don't have defaults set
    try:
        # geef alle lijnen die een gemeente bedienen
        api_response = api_instance.geef_lijnen_voor_gemeente(gemeente_nummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling GemeentenApi->geef_lijnen_voor_gemeente: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gemeente_nummer** | **int**| Format - int32. nummer van de gemeente |

### Return type

[**Lijnen**](Lijnen.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | gemeente is niet gevonden |  -  |
**500** | service of achterliggende systemen niet beschikbaar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

