# delijn_api_kern.OmleidingenApi

All URIs are relative to *https://api.delijn.be/DLKernOpenData/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geef_omleiding**](OmleidingenApi.md#geef_omleiding) | **GET** /omleidingen/{referentieOmleiding} | geef de omleiding op basis van zijn referentie id
[**geef_omleidingen**](OmleidingenApi.md#geef_omleidingen) | **GET** /omleidingen | geef alle omleidingen voor een periode van hoogstens een maand


# **geef_omleiding**
> Omleiding geef_omleiding(referentie_omleiding)

geef de omleiding op basis van zijn referentie id

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import omleidingen_api
from delijn_api_kern.model.omleiding import Omleiding
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
    api_instance = omleidingen_api.OmleidingenApi(api_client)
    referentie_omleiding = 1 # int | Format - int32. referentie id van de omleiding
    taal_code = "NEDERLANDS" # str | de taalcode voor de titel en omschrijving van de omleidingen (optional) if omitted the server will use the default value of "NEDERLANDS"

    # example passing only required values which don't have defaults set
    try:
        # geef de omleiding op basis van zijn referentie id
        api_response = api_instance.geef_omleiding(referentie_omleiding)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling OmleidingenApi->geef_omleiding: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef de omleiding op basis van zijn referentie id
        api_response = api_instance.geef_omleiding(referentie_omleiding, taal_code=taal_code)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling OmleidingenApi->geef_omleiding: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **referentie_omleiding** | **int**| Format - int32. referentie id van de omleiding |
 **taal_code** | **str**| de taalcode voor de titel en omschrijving van de omleidingen | [optional] if omitted the server will use the default value of "NEDERLANDS"

### Return type

[**Omleiding**](Omleiding.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | request met succes afgehandeld |  -  |
**404** | omleiding is niet gevonden |  -  |
**500** | service of achterliggende systemen niet beschikbaar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geef_omleidingen**
> Omleidingen geef_omleidingen()

geef alle omleidingen voor een periode van hoogstens een maand

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import omleidingen_api
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
    api_instance = omleidingen_api.OmleidingenApi(api_client)
    start_datum = "startDatum_example" # str | tijdstip in formaat yyyy-MM-dd'T'HH:mm:ss als start moment voor de opzoeking van de omleidingen met als default waarde de huidige tijdstip (optional)
    eind_datum = "eindDatum_example" # str | tijdstip in formaat yyyy-MM-dd'T'HH:mm:ss als eind moment voor de opzoeking van de omleidingen  met als default waarde de huidige tijdstip (optional)
    taal_code = "NEDERLANDS" # str | de taalcode voor de titel en omschrijving van de omleidingen (optional) if omitted the server will use the default value of "NEDERLANDS"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef alle omleidingen voor een periode van hoogstens een maand
        api_response = api_instance.geef_omleidingen(start_datum=start_datum, eind_datum=eind_datum, taal_code=taal_code)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling OmleidingenApi->geef_omleidingen: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_datum** | **str**| tijdstip in formaat yyyy-MM-dd&#39;T&#39;HH:mm:ss als start moment voor de opzoeking van de omleidingen met als default waarde de huidige tijdstip | [optional]
 **eind_datum** | **str**| tijdstip in formaat yyyy-MM-dd&#39;T&#39;HH:mm:ss als eind moment voor de opzoeking van de omleidingen  met als default waarde de huidige tijdstip | [optional]
 **taal_code** | **str**| de taalcode voor de titel en omschrijving van de omleidingen | [optional] if omitted the server will use the default value of "NEDERLANDS"

### Return type

[**Omleidingen**](Omleidingen.md)

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

