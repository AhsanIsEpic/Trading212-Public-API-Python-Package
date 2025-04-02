<a id="__pageTop"></a>
# openapi_client.apis.tags.instruments_metadata_api.InstrumentsMetadataApi

All URIs are relative to *https://demo.trading212.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchanges**](#exchanges) | **get** /api/v0/equity/metadata/exchanges | Exchange List
[**instruments**](#instruments) | **get** /api/v0/equity/metadata/instruments | Instrument List

# **exchanges**
<a id="exchanges"></a>
> [Exchange] exchanges()

Exchange List

Fetch all exchanges and their corresponding working schedules that your account has access to

### Example

* Api Key Authentication (apiKeyHeader):
```python
import openapi_client
from openapi_client.apis.tags import instruments_metadata_api
from openapi_client.model.exchange import Exchange
from pprint import pprint
# Defining the host is optional and defaults to https://demo.trading212.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo.trading212.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = instruments_metadata_api.InstrumentsMetadataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Exchange List
        api_response = api_instance.exchanges()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InstrumentsMetadataApi->exchanges: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#exchanges.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#exchanges.ApiResponseFor401) | Bad API key
403 | [ApiResponseFor403](#exchanges.ApiResponseFor403) | Scope( metadata ) missing for API key
408 | [ApiResponseFor408](#exchanges.ApiResponseFor408) | Timed-out
429 | [ApiResponseFor429](#exchanges.ApiResponseFor429) | Limited: 1 / 30s

#### exchanges.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Exchange**]({{complexTypePrefix}}Exchange.md) | [**Exchange**]({{complexTypePrefix}}Exchange.md) | [**Exchange**]({{complexTypePrefix}}Exchange.md) |  | 

#### exchanges.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### exchanges.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### exchanges.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### exchanges.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apiKeyHeader](../../../README.md#apiKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **instruments**
<a id="instruments"></a>
> [TradeableInstrument] instruments()

Instrument List

Fetch all instruments that your account has access to

### Example

* Api Key Authentication (apiKeyHeader):
```python
import openapi_client
from openapi_client.apis.tags import instruments_metadata_api
from openapi_client.model.tradeable_instrument import TradeableInstrument
from pprint import pprint
# Defining the host is optional and defaults to https://demo.trading212.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo.trading212.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = instruments_metadata_api.InstrumentsMetadataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Instrument List
        api_response = api_instance.instruments()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InstrumentsMetadataApi->instruments: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#instruments.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#instruments.ApiResponseFor401) | Bad API key
403 | [ApiResponseFor403](#instruments.ApiResponseFor403) | Scope( metadata ) missing for API key
408 | [ApiResponseFor408](#instruments.ApiResponseFor408) | Timed-out
429 | [ApiResponseFor429](#instruments.ApiResponseFor429) | Limited: 1 / 50s

#### instruments.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TradeableInstrument**]({{complexTypePrefix}}TradeableInstrument.md) | [**TradeableInstrument**]({{complexTypePrefix}}TradeableInstrument.md) | [**TradeableInstrument**]({{complexTypePrefix}}TradeableInstrument.md) |  | 

#### instruments.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### instruments.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### instruments.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### instruments.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apiKeyHeader](../../../README.md#apiKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

