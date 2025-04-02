<a id="__pageTop"></a>
# openapi_client.apis.tags.account_data_api.AccountDataApi

All URIs are relative to *https://demo.trading212.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account**](#account) | **get** /api/v0/equity/account/info | Fetch account metadata
[**account_cash**](#account_cash) | **get** /api/v0/equity/account/cash | Fetch account cash

# **account**
<a id="account"></a>
> Account account()

Fetch account metadata

### Example

* Api Key Authentication (apiKeyHeader):
```python
import openapi_client
from openapi_client.apis.tags import account_data_api
from openapi_client.model.account import Account
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
    api_instance = account_data_api.AccountDataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch account metadata
        api_response = api_instance.account()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountDataApi->account: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#account.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#account.ApiResponseFor401) | Bad API key
403 | [ApiResponseFor403](#account.ApiResponseFor403) | Scope( account ) missing for API key
408 | [ApiResponseFor408](#account.ApiResponseFor408) | Timed-out
429 | [ApiResponseFor429](#account.ApiResponseFor429) | Limited: 1 / 30s

#### account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Account**](../../models/Account.md) |  | 


#### account.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### account.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### account.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### account.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apiKeyHeader](../../../README.md#apiKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **account_cash**
<a id="account_cash"></a>
> Cash account_cash()

Fetch account cash

### Example

* Api Key Authentication (apiKeyHeader):
```python
import openapi_client
from openapi_client.apis.tags import account_data_api
from openapi_client.model.cash import Cash
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
    api_instance = account_data_api.AccountDataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch account cash
        api_response = api_instance.account_cash()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountDataApi->account_cash: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#account_cash.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#account_cash.ApiResponseFor401) | Bad API key
403 | [ApiResponseFor403](#account_cash.ApiResponseFor403) | Scope( account ) missing for API key
408 | [ApiResponseFor408](#account_cash.ApiResponseFor408) | Timed-out
429 | [ApiResponseFor429](#account_cash.ApiResponseFor429) | Limited: 1 / 2s

#### account_cash.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Cash**](../../models/Cash.md) |  | 


#### account_cash.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### account_cash.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### account_cash.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### account_cash.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[apiKeyHeader](../../../README.md#apiKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

