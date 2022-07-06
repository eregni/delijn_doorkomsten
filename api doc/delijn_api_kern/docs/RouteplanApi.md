# delijn_api_kern.RouteplanApi

All URIs are relative to *https://api.delijn.be/DLKernOpenData/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geef_routeplan**](RouteplanApi.md#geef_routeplan) | **GET** /routeplan/{vertrekLatlng}/{bestemmingLatlng} | geef een initëel, vroeger, later of laatste routeplan 


# **geef_routeplan**
> Routeplan geef_routeplan(vertrek_latlng, bestemming_latlng)

geef een initëel, vroeger, later of laatste routeplan 

voor een vroeger routeplan dient de parameter tijdstip overeen te komen met het aankomsttijdsip (duurtijd.einde) van de vroegste reisweg, voor een later routeplan dient de parameter tijdstip overeen te komen het het vertrektijdstip (duurtijd.start) van de laatste reisweg

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (apiKeyQuery):

```python
import time
import delijn_api_kern
from delijn_api_kern.api import routeplan_api
from delijn_api_kern.model.routeplan import Routeplan
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
    api_instance = routeplan_api.RouteplanApi(api_client)
    vertrek_latlng = "vertrekLatlng_example" # str | latitude en longitude van de vertrek locatie gescheiden door komma bv, 51.056064,3.797336
    bestemming_latlng = "bestemmingLatlng_example" # str | latitude en longitude van de aankomst locatie gescheiden door komma bv, 51.056064,3.797336
    aanvraag_type = "INITIEEL" # str | bepaalt of de aanvraag gaat over een initiële, vroegere, latere of laatste routeplan (optional) if omitted the server will use the default value of "INITIEEL"
    tijdstip = "tijdstip_example" # str | tijdstip van vertrekken of aankomen in formaat yyyy-MM-dd'T'HH:mm:ss bv. 2016-11-11T22:00:00 (optional)
    vertrek_aankomst = "VERTREK" # str | verwijst het tijdstip naar het moment van vertrek of aankomst (optional) if omitted the server will use the default value of "VERTREK"
    vervoers_optie = [
        "BUS",
    ] # [str] | Lijst van vervoersopties met als default BUS,TRAM,METRO en TREIN (optional)

    # example passing only required values which don't have defaults set
    try:
        # geef een initëel, vroeger, later of laatste routeplan 
        api_response = api_instance.geef_routeplan(vertrek_latlng, bestemming_latlng)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling RouteplanApi->geef_routeplan: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # geef een initëel, vroeger, later of laatste routeplan 
        api_response = api_instance.geef_routeplan(vertrek_latlng, bestemming_latlng, aanvraag_type=aanvraag_type, tijdstip=tijdstip, vertrek_aankomst=vertrek_aankomst, vervoers_optie=vervoers_optie)
        pprint(api_response)
    except delijn_api_kern.ApiException as e:
        print("Exception when calling RouteplanApi->geef_routeplan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vertrek_latlng** | **str**| latitude en longitude van de vertrek locatie gescheiden door komma bv, 51.056064,3.797336 |
 **bestemming_latlng** | **str**| latitude en longitude van de aankomst locatie gescheiden door komma bv, 51.056064,3.797336 |
 **aanvraag_type** | **str**| bepaalt of de aanvraag gaat over een initiële, vroegere, latere of laatste routeplan | [optional] if omitted the server will use the default value of "INITIEEL"
 **tijdstip** | **str**| tijdstip van vertrekken of aankomen in formaat yyyy-MM-dd&#39;T&#39;HH:mm:ss bv. 2016-11-11T22:00:00 | [optional]
 **vertrek_aankomst** | **str**| verwijst het tijdstip naar het moment van vertrek of aankomst | [optional] if omitted the server will use the default value of "VERTREK"
 **vervoers_optie** | **[str]**| Lijst van vervoersopties met als default BUS,TRAM,METRO en TREIN | [optional]

### Return type

[**Routeplan**](Routeplan.md)

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

