# delijn_api_kern.EntiteitenApi

All URIs are relative to *https://api.delijn.be/DLKernOpenData/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geef_entiteit**](EntiteitenApi.md#geef_entiteit) | **GET** /entiteiten/{entiteitnummer} | geef een entiteit op basis van het opgegeven entiteitnummer
[**geef_entiteiten**](EntiteitenApi.md#geef_entiteiten) | **GET** /entiteiten | geef alle entiteiten
[**geef_gemeenten_voor_entiteit**](EntiteitenApi.md#geef_gemeenten_voor_entiteit) | **GET** /entiteiten/{entiteitnummer}/gemeenten | geef alle gemeenten die beheerd worden door een entiteit
[**geef_haltes_voor_entiteit**](EntiteitenApi.md#geef_haltes_voor_entiteit) | **GET** /entiteiten/{entiteitnummer}/haltes | geef alle haltes die beheerd worden door een entiteit
[**geef_lijnen_voor_entiteit**](EntiteitenApi.md#geef_lijnen_voor_entiteit) | **GET** /entiteiten/{entiteitnummer}/lijnen | geef alle lijnen die beheerd worden door een entiteit


# **geef_entiteit**
> Entiteit geef_entiteit(entiteitnummer)

geef een entiteit op basis van het opgegeven entiteitnummer

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import entiteiten_api
from delijn_api_kern.model.entiteit import Entiteit
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
    api_instance = entiteiten_api.EntiteitenApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit

    # example passing only required values which don't have defaults set
    try:
        # geef een entiteit op basis van het opgegeven entiteitnummer
        api_response = api_instance.geef_entiteit(entiteitnummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling EntiteitenApi->geef_entiteit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |

### Return type

[**Entiteit**](Entiteit.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | entiteit is niet gevonden |  -  |
**500** | service of achterliggende systemen niet beschikbaar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_entiteiten**
> Entiteiten geef_entiteiten()

geef alle entiteiten

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import entiteiten_api
from delijn_api_kern.model.entiteiten import Entiteiten
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
    api_instance = entiteiten_api.EntiteitenApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # geef alle entiteiten
        api_response = api_instance.geef_entiteiten()
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling EntiteitenApi->geef_entiteiten: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Entiteiten**](Entiteiten.md)

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

# **geef_gemeenten_voor_entiteit**
> Gemeenten geef_gemeenten_voor_entiteit(entiteitnummer)

geef alle gemeenten die beheerd worden door een entiteit

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import entiteiten_api
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
    api_instance = entiteiten_api.EntiteitenApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit

    # example passing only required values which don't have defaults set
    try:
        # geef alle gemeenten die beheerd worden door een entiteit
        api_response = api_instance.geef_gemeenten_voor_entiteit(entiteitnummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling EntiteitenApi->geef_gemeenten_voor_entiteit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |

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

# **geef_haltes_voor_entiteit**
> Haltes geef_haltes_voor_entiteit(entiteitnummer)

geef alle haltes die beheerd worden door een entiteit

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import entiteiten_api
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
    api_instance = entiteiten_api.EntiteitenApi(api_client)
    entiteitnummer = 1 # int | Format - int32. nummer van de entiteit

    # example passing only required values which don't have defaults set
    try:
        # geef alle haltes die beheerd worden door een entiteit
        api_response = api_instance.geef_haltes_voor_entiteit(entiteitnummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling EntiteitenApi->geef_haltes_voor_entiteit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **int**| Format - int32. nummer van de entiteit |

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

# **geef_lijnen_voor_entiteit**
> Lijnen geef_lijnen_voor_entiteit(entiteitnummer)

geef alle lijnen die beheerd worden door een entiteit

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import entiteiten_api
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
    api_instance = entiteiten_api.EntiteitenApi(api_client)
    entiteitnummer = "entiteitnummer_example" # str | nummer van de entiteit

    # example passing only required values which don't have defaults set
    try:
        # geef alle lijnen die beheerd worden door een entiteit
        api_response = api_instance.geef_lijnen_voor_entiteit(entiteitnummer)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling EntiteitenApi->geef_lijnen_voor_entiteit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entiteitnummer** | **str**| nummer van de entiteit |

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
**500** | service of achterliggende systemen niet beschikbaar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

