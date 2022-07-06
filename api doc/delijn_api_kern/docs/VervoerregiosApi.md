# delijn_api_kern.VervoerregiosApi

All URIs are relative to *https://api.delijn.be/DLKernOpenData/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geef_lijnen_voor_vervoer_regio**](VervoerregiosApi.md#geef_lijnen_voor_vervoer_regio) | **GET** /vervoerregios/{code}/lijnen | geef alle lijnen in een vervoerregio
[**geef_vervoer_regio**](VervoerregiosApi.md#geef_vervoer_regio) | **GET** /vervoerregios/{code} | geef vervoerregio
[**geef_vervoer_regios**](VervoerregiosApi.md#geef_vervoer_regios) | **GET** /vervoerregios | geef alle vervoerregios


# **geef_lijnen_voor_vervoer_regio**
> Lijnen geef_lijnen_voor_vervoer_regio(code)

geef alle lijnen in een vervoerregio

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import vervoerregios_api
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
    api_instance = vervoerregios_api.VervoerregiosApi(api_client)
    code = "code_example" # str | vervoerregio code

    # example passing only required values which don't have defaults set
    try:
        # geef alle lijnen in een vervoerregio
        api_response = api_instance.geef_lijnen_voor_vervoer_regio(code)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling VervoerregiosApi->geef_lijnen_voor_vervoer_regio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| vervoerregio code |

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

# **geef_vervoer_regio**
> VervoerRegio geef_vervoer_regio(code)

geef vervoerregio

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import vervoerregios_api
from delijn_api_kern.model.vervoer_regio import VervoerRegio
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
    api_instance = vervoerregios_api.VervoerregiosApi(api_client)
    code = "code_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # geef vervoerregio
        api_response = api_instance.geef_vervoer_regio(code)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling VervoerregiosApi->geef_vervoer_regio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  |

### Return type

[**VervoerRegio**](VervoerRegio.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | request met succes afgehandeld |  -  |
**400** | ongeldige input waarden in de request |  -  |
**500** | service of achterliggende systemen niet beschikbaar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_vervoer_regios**
> VervoerRegios geef_vervoer_regios()

geef alle vervoerregios

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import vervoerregios_api
from delijn_api_kern.model.vervoer_regios import VervoerRegios
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
    api_instance = vervoerregios_api.VervoerregiosApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # geef alle vervoerregios
        api_response = api_instance.geef_vervoer_regios()
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling VervoerregiosApi->geef_vervoer_regios: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**VervoerRegios**](VervoerRegios.md)

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

