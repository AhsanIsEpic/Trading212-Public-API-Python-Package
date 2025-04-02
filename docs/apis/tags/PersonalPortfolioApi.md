<a id="__pageTop"></a>
# openapi_client.apis.tags.personal_portfolio_api.PersonalPortfolioApi

All URIs are relative to *https://demo.trading212.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portfolio**](#portfolio) | **get** /api/v0/equity/portfolio | Fetch all open positions
[**position_by_ticker**](#position_by_ticker) | **get** /api/v0/equity/portfolio/{ticker} | Fetch a specific position
[**position_by_ticker_v2**](#position_by_ticker_v2) | **post** /api/v0/equity/portfolio/ticker | Search for a specific position by ticker

# **portfolio**
<a id="portfolio"></a>
> [Position] portfolio()

Fetch all open positions

Fetch an open positions for your account

### Example

* Api Key Authentication (apiKeyHeader):
```python
import openapi_client
from openapi_client.apis.tags import personal_portfolio_api
from openapi_client.model.position import Position
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
    api_instance = personal_portfolio_api.PersonalPortfolioApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch all open positions
        api_response = api_instance.portfolio()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PersonalPortfolioApi->portfolio: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#portfolio.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#portfolio.ApiResponseFor401) | Bad API key
403 | [ApiResponseFor403](#portfolio.ApiResponseFor403) | Scope( portfolio ) missing for API key
408 | [ApiResponseFor408](#portfolio.ApiResponseFor408) | Timed-out
429 | [ApiResponseFor429](#portfolio.ApiResponseFor429) | Limited: 1 / 5s

#### portfolio.ApiResponseFor200
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
[**Position**]({{complexTypePrefix}}Position.md) | [**Position**]({{complexTypePrefix}}Position.md) | [**Position**]({{complexTypePrefix}}Position.md) |  | 

#### portfolio.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### portfolio.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### portfolio.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### portfolio.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apiKeyHeader](../../../README.md#apiKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **position_by_ticker**
<a id="position_by_ticker"></a>
> Position position_by_ticker(ticker)

Fetch a specific position

Fetch an open position by ticker

### Example

* Api Key Authentication (apiKeyHeader):
```python
import openapi_client
from openapi_client.apis.tags import personal_portfolio_api
from openapi_client.model.position import Position
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
    api_instance = personal_portfolio_api.PersonalPortfolioApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ticker': "AAPL_US_EQ",
    }
    try:
        # Fetch a specific position
        api_response = api_instance.position_by_ticker(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PersonalPortfolioApi->position_by_ticker: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ticker | TickerSchema | | 

# TickerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#position_by_ticker.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#position_by_ticker.ApiResponseFor400) | Invalid ticker supplied
401 | [ApiResponseFor401](#position_by_ticker.ApiResponseFor401) | Bad API key
403 | [ApiResponseFor403](#position_by_ticker.ApiResponseFor403) | Scope( portfolio ) missing for API key
404 | [ApiResponseFor404](#position_by_ticker.ApiResponseFor404) | No open position with that ticker
408 | [ApiResponseFor408](#position_by_ticker.ApiResponseFor408) | Timed-out
429 | [ApiResponseFor429](#position_by_ticker.ApiResponseFor429) | Limited: 1 / 1s

#### position_by_ticker.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Position**](../../models/Position.md) |  | 


#### position_by_ticker.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### position_by_ticker.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### position_by_ticker.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### position_by_ticker.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### position_by_ticker.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### position_by_ticker.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apiKeyHeader](../../../README.md#apiKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **position_by_ticker_v2**
<a id="position_by_ticker_v2"></a>
> Position position_by_ticker_v2(position_request)

Search for a specific position by ticker

Search for a open position by ticker

### Example

* Api Key Authentication (apiKeyHeader):
```python
import openapi_client
from openapi_client.apis.tags import personal_portfolio_api
from openapi_client.model.position import Position
from openapi_client.model.position_request import PositionRequest
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
    api_instance = personal_portfolio_api.PersonalPortfolioApi(api_client)

    # example passing only required values which don't have defaults set
    body = PositionRequest(
        ticker="ticker_example",
    )
    try:
        # Search for a specific position by ticker
        api_response = api_instance.position_by_ticker_v2(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PersonalPortfolioApi->position_by_ticker_v2: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PositionRequest**](../../models/PositionRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#position_by_ticker_v2.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#position_by_ticker_v2.ApiResponseFor400) | Invalid ticker supplied
401 | [ApiResponseFor401](#position_by_ticker_v2.ApiResponseFor401) | Bad API key
403 | [ApiResponseFor403](#position_by_ticker_v2.ApiResponseFor403) | Scope( portfolio ) missing for API key
404 | [ApiResponseFor404](#position_by_ticker_v2.ApiResponseFor404) | No open position with that ticker
408 | [ApiResponseFor408](#position_by_ticker_v2.ApiResponseFor408) | Timed-out
429 | [ApiResponseFor429](#position_by_ticker_v2.ApiResponseFor429) | Limited: 1 / 1s

#### position_by_ticker_v2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Position**](../../models/Position.md) |  | 


#### position_by_ticker_v2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### position_by_ticker_v2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### position_by_ticker_v2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### position_by_ticker_v2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### position_by_ticker_v2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### position_by_ticker_v2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apiKeyHeader](../../../README.md#apiKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

