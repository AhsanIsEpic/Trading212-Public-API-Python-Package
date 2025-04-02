<a id="__pageTop"></a>
# openapi_client.apis.tags.historical_items_api.HistoricalItemsApi

All URIs are relative to *https://demo.trading212.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dividends**](#dividends) | **get** /api/v0/history/dividends | Paid out dividends
[**get_reports**](#get_reports) | **get** /api/v0/history/exports | Exports List
[**orders1**](#orders1) | **get** /api/v0/equity/history/orders | Historical order data
[**request_report**](#request_report) | **post** /api/v0/history/exports | Export csv
[**transactions**](#transactions) | **get** /api/v0/history/transactions | Transaction list

# **dividends**
<a id="dividends"></a>
> PaginatedResponseHistoryDividendItem dividends()

Paid out dividends

### Example

* Api Key Authentication (apiKeyHeader):
```python
import openapi_client
from openapi_client.apis.tags import historical_items_api
from openapi_client.model.paginated_response_history_dividend_item import PaginatedResponseHistoryDividendItem
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
    api_instance = historical_items_api.HistoricalItemsApi(api_client)

    # example passing only optional values
    query_params = {
        'cursor': 1,
        'ticker': "ticker_example",
        'limit': 21,
    }
    try:
        # Paid out dividends
        api_response = api_instance.dividends(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HistoricalItemsApi->dividends: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cursor | CursorSchema | | optional
ticker | TickerSchema | | optional
limit | LimitSchema | | optional


# CursorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# TickerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 20value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#dividends.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#dividends.ApiResponseFor400) | Bad filtering arguments
401 | [ApiResponseFor401](#dividends.ApiResponseFor401) | Bad API key
403 | [ApiResponseFor403](#dividends.ApiResponseFor403) | Scope( history:dividends ) missing for API key
408 | [ApiResponseFor408](#dividends.ApiResponseFor408) | Timed-out
429 | [ApiResponseFor429](#dividends.ApiResponseFor429) | Limited: 6 / 1m0s

#### dividends.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedResponseHistoryDividendItem**](../../models/PaginatedResponseHistoryDividendItem.md) |  | 


#### dividends.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### dividends.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### dividends.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### dividends.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### dividends.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apiKeyHeader](../../../README.md#apiKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_reports**
<a id="get_reports"></a>
> [ReportResponse] get_reports()

Exports List

Lists detailed information about all csv account exports

### Example

* Api Key Authentication (apiKeyHeader):
```python
import openapi_client
from openapi_client.apis.tags import historical_items_api
from openapi_client.model.report_response import ReportResponse
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
    api_instance = historical_items_api.HistoricalItemsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Exports List
        api_response = api_instance.get_reports()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HistoricalItemsApi->get_reports: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_reports.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_reports.ApiResponseFor400) | Bad filtering arguments
401 | [ApiResponseFor401](#get_reports.ApiResponseFor401) | Bad API key
403 | [ApiResponseFor403](#get_reports.ApiResponseFor403) | Missing Permissions
408 | [ApiResponseFor408](#get_reports.ApiResponseFor408) | Timed-out
429 | [ApiResponseFor429](#get_reports.ApiResponseFor429) | Limited: 1 / 1m0s

#### get_reports.ApiResponseFor200
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
[**ReportResponse**]({{complexTypePrefix}}ReportResponse.md) | [**ReportResponse**]({{complexTypePrefix}}ReportResponse.md) | [**ReportResponse**]({{complexTypePrefix}}ReportResponse.md) |  | 

#### get_reports.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_reports.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_reports.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_reports.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_reports.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apiKeyHeader](../../../README.md#apiKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **orders1**
<a id="orders1"></a>
> PaginatedResponseHistoricalOrder orders1()

Historical order data

### Example

* Api Key Authentication (apiKeyHeader):
```python
import openapi_client
from openapi_client.apis.tags import historical_items_api
from openapi_client.model.paginated_response_historical_order import PaginatedResponseHistoricalOrder
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
    api_instance = historical_items_api.HistoricalItemsApi(api_client)

    # example passing only optional values
    query_params = {
        'cursor': 1,
        'ticker': "ticker_example",
        'limit': 21,
    }
    try:
        # Historical order data
        api_response = api_instance.orders1(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HistoricalItemsApi->orders1: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cursor | CursorSchema | | optional
ticker | TickerSchema | | optional
limit | LimitSchema | | optional


# CursorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# TickerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 20value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#orders1.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#orders1.ApiResponseFor400) | Bad filtering arguments
401 | [ApiResponseFor401](#orders1.ApiResponseFor401) | Bad API key
403 | [ApiResponseFor403](#orders1.ApiResponseFor403) | Scope( history:orders ) missing for API key
408 | [ApiResponseFor408](#orders1.ApiResponseFor408) | Timed-out
429 | [ApiResponseFor429](#orders1.ApiResponseFor429) | Limited: 6 / 1m0s

#### orders1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedResponseHistoricalOrder**](../../models/PaginatedResponseHistoricalOrder.md) |  | 


#### orders1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### orders1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### orders1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### orders1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### orders1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apiKeyHeader](../../../README.md#apiKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **request_report**
<a id="request_report"></a>
> EnqueuedReportResponse request_report(public_report_request)

Export csv

Request a csv export of the account's orders, dividends and transactions history

### Example

* Api Key Authentication (apiKeyHeader):
```python
import openapi_client
from openapi_client.apis.tags import historical_items_api
from openapi_client.model.public_report_request import PublicReportRequest
from openapi_client.model.enqueued_report_response import EnqueuedReportResponse
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
    api_instance = historical_items_api.HistoricalItemsApi(api_client)

    # example passing only required values which don't have defaults set
    body = PublicReportRequest(
        data_included=ReportDataIncluded(
            include_dividends=True,
            include_interest=True,
            include_orders=True,
            include_transactions=True,
        ),
        time_from="1970-01-01T00:00:00.00Z",
        time_to="1970-01-01T00:00:00.00Z",
    )
    try:
        # Export csv
        api_response = api_instance.request_report(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HistoricalItemsApi->request_report: %s\n" % e)
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
[**PublicReportRequest**](../../models/PublicReportRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#request_report.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#request_report.ApiResponseFor400) | Bad filtering arguments
401 | [ApiResponseFor401](#request_report.ApiResponseFor401) | Bad API key
403 | [ApiResponseFor403](#request_report.ApiResponseFor403) | Missing Permissions
408 | [ApiResponseFor408](#request_report.ApiResponseFor408) | Timed-out
429 | [ApiResponseFor429](#request_report.ApiResponseFor429) | Limited: 1 / 30s

#### request_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnqueuedReportResponse**](../../models/EnqueuedReportResponse.md) |  | 


#### request_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### request_report.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### request_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### request_report.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### request_report.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apiKeyHeader](../../../README.md#apiKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **transactions**
<a id="transactions"></a>
> PaginatedResponseHistoryTransactionItem transactions()

Transaction list

Fetch superficial information about movements to and from your account

### Example

* Api Key Authentication (apiKeyHeader):
```python
import openapi_client
from openapi_client.apis.tags import historical_items_api
from openapi_client.model.paginated_response_history_transaction_item import PaginatedResponseHistoryTransactionItem
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
    api_instance = historical_items_api.HistoricalItemsApi(api_client)

    # example passing only optional values
    query_params = {
        'cursor': "cursor_example",
        'time': "1970-01-01T00:00:00.00Z",
        'limit': 21,
    }
    try:
        # Transaction list
        api_response = api_instance.transactions(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HistoricalItemsApi->transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cursor | CursorSchema | | optional
time | TimeSchema | | optional
limit | LimitSchema | | optional


# CursorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 20value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#transactions.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#transactions.ApiResponseFor400) | Bad filtering arguments
401 | [ApiResponseFor401](#transactions.ApiResponseFor401) | Bad API key
403 | [ApiResponseFor403](#transactions.ApiResponseFor403) | Scope( history:transactions ) missing for API key
408 | [ApiResponseFor408](#transactions.ApiResponseFor408) | Timed-out
429 | [ApiResponseFor429](#transactions.ApiResponseFor429) | Limited: 6 / 1m0s

#### transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedResponseHistoryTransactionItem**](../../models/PaginatedResponseHistoryTransactionItem.md) |  | 


#### transactions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### transactions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### transactions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### transactions.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### transactions.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apiKeyHeader](../../../README.md#apiKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

