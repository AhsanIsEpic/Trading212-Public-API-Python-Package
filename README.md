# Trading212 Public API Python Package
A Python packaged generated using the OpenAPI specification for Trading212 Public API [v0]. Available at https://t212public-api-docs.redoc.ly/

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0
- Package version: 0.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.10

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/AhsanIsEpic/Trading212-Public-API-Python-Package.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/AhsanIsEpic/Trading212-Public-API-Python-Package.git`)

Then import the package:
```python
import trading212_api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import trading212_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import trading212_api_client
from pprint import pprint
from trading212_api_client.apis.tags import account_data_api
from trading212_api_client.model.account import Account
from trading212_api_client.model.cash import Cash
# Defining the host is optional and defaults to https://demo.trading212.com
# See configuration.py for a list of all supported configuration parameters.
configuration = trading212_api_client.Configuration(
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
with trading212_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_data_api.AccountDataApi(api_client)
    
    try:
        # Fetch account metadata
        api_response = api_instance.account()
        pprint(api_response)
    except trading212_api_client.ApiException as e:
        print("Exception when calling AccountDataApi->account: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://demo.trading212.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountDataApi* | [**account**](docs/apis/tags/AccountDataApi.md#account) | **get** /api/v0/equity/account/info | Fetch account metadata
*AccountDataApi* | [**account_cash**](docs/apis/tags/AccountDataApi.md#account_cash) | **get** /api/v0/equity/account/cash | Fetch account cash
*EquityOrdersApi* | [**cancel_order**](docs/apis/tags/EquityOrdersApi.md#cancel_order) | **delete** /api/v0/equity/orders/{id} | Cancel by ID
*EquityOrdersApi* | [**order_by_id**](docs/apis/tags/EquityOrdersApi.md#order_by_id) | **get** /api/v0/equity/orders/{id} | Fetch by ID
*EquityOrdersApi* | [**orders**](docs/apis/tags/EquityOrdersApi.md#orders) | **get** /api/v0/equity/orders | Fetch all
*EquityOrdersApi* | [**place_limit_order**](docs/apis/tags/EquityOrdersApi.md#place_limit_order) | **post** /api/v0/equity/orders/limit | Place Limit order
*EquityOrdersApi* | [**place_market_order**](docs/apis/tags/EquityOrdersApi.md#place_market_order) | **post** /api/v0/equity/orders/market | Place Market order
*EquityOrdersApi* | [**place_stop_order**](docs/apis/tags/EquityOrdersApi.md#place_stop_order) | **post** /api/v0/equity/orders/stop_limit | Place StopLimit order
*EquityOrdersApi* | [**place_stop_order1**](docs/apis/tags/EquityOrdersApi.md#place_stop_order1) | **post** /api/v0/equity/orders/stop | Place Stop order
*HistoricalItemsApi* | [**dividends**](docs/apis/tags/HistoricalItemsApi.md#dividends) | **get** /api/v0/history/dividends | Paid out dividends
*HistoricalItemsApi* | [**get_reports**](docs/apis/tags/HistoricalItemsApi.md#get_reports) | **get** /api/v0/history/exports | Exports List
*HistoricalItemsApi* | [**orders1**](docs/apis/tags/HistoricalItemsApi.md#orders1) | **get** /api/v0/equity/history/orders | Historical order data
*HistoricalItemsApi* | [**request_report**](docs/apis/tags/HistoricalItemsApi.md#request_report) | **post** /api/v0/history/exports | Export csv
*HistoricalItemsApi* | [**transactions**](docs/apis/tags/HistoricalItemsApi.md#transactions) | **get** /api/v0/history/transactions | Transaction list
*InstrumentsMetadataApi* | [**exchanges**](docs/apis/tags/InstrumentsMetadataApi.md#exchanges) | **get** /api/v0/equity/metadata/exchanges | Exchange List
*InstrumentsMetadataApi* | [**instruments**](docs/apis/tags/InstrumentsMetadataApi.md#instruments) | **get** /api/v0/equity/metadata/instruments | Instrument List
*PersonalPortfolioApi* | [**portfolio**](docs/apis/tags/PersonalPortfolioApi.md#portfolio) | **get** /api/v0/equity/portfolio | Fetch all open positions
*PersonalPortfolioApi* | [**position_by_ticker**](docs/apis/tags/PersonalPortfolioApi.md#position_by_ticker) | **get** /api/v0/equity/portfolio/{ticker} | Fetch a specific position
*PersonalPortfolioApi* | [**position_by_ticker_v2**](docs/apis/tags/PersonalPortfolioApi.md#position_by_ticker_v2) | **post** /api/v0/equity/portfolio/ticker | Search for a specific position by ticker
*PiesApi* | [**create**](docs/apis/tags/PiesApi.md#create) | **post** /api/v0/equity/pies | Create pie
*PiesApi* | [**delete**](docs/apis/tags/PiesApi.md#delete) | **delete** /api/v0/equity/pies/{id} | Delete pie
*PiesApi* | [**duplicate_pie**](docs/apis/tags/PiesApi.md#duplicate_pie) | **post** /api/v0/equity/pies/{id}/duplicate | Duplicate pie
*PiesApi* | [**get_all**](docs/apis/tags/PiesApi.md#get_all) | **get** /api/v0/equity/pies | Fetch all pies
*PiesApi* | [**get_detailed**](docs/apis/tags/PiesApi.md#get_detailed) | **get** /api/v0/equity/pies/{id} | Fetch a pie
*PiesApi* | [**update**](docs/apis/tags/PiesApi.md#update) | **post** /api/v0/equity/pies/{id} | Update pie

## Documentation For Models

 - [Account](docs/models/Account.md)
 - [AccountBucketDetailedResponse](docs/models/AccountBucketDetailedResponse.md)
 - [AccountBucketInstrumentResult](docs/models/AccountBucketInstrumentResult.md)
 - [AccountBucketInstrumentsDetailedResponse](docs/models/AccountBucketInstrumentsDetailedResponse.md)
 - [AccountBucketResultResponse](docs/models/AccountBucketResultResponse.md)
 - [Cash](docs/models/Cash.md)
 - [DividendDetails](docs/models/DividendDetails.md)
 - [DuplicateBucketRequest](docs/models/DuplicateBucketRequest.md)
 - [EnqueuedReportResponse](docs/models/EnqueuedReportResponse.md)
 - [Exchange](docs/models/Exchange.md)
 - [HistoricalOrder](docs/models/HistoricalOrder.md)
 - [HistoryDividendItem](docs/models/HistoryDividendItem.md)
 - [HistoryTransactionItem](docs/models/HistoryTransactionItem.md)
 - [InstrumentIssue](docs/models/InstrumentIssue.md)
 - [InvestmentResult](docs/models/InvestmentResult.md)
 - [LimitRequest](docs/models/LimitRequest.md)
 - [MarketRequest](docs/models/MarketRequest.md)
 - [Order](docs/models/Order.md)
 - [PaginatedResponseHistoricalOrder](docs/models/PaginatedResponseHistoricalOrder.md)
 - [PaginatedResponseHistoryDividendItem](docs/models/PaginatedResponseHistoryDividendItem.md)
 - [PaginatedResponseHistoryTransactionItem](docs/models/PaginatedResponseHistoryTransactionItem.md)
 - [PieRequest](docs/models/PieRequest.md)
 - [PlaceOrderError](docs/models/PlaceOrderError.md)
 - [Position](docs/models/Position.md)
 - [PositionRequest](docs/models/PositionRequest.md)
 - [PublicReportRequest](docs/models/PublicReportRequest.md)
 - [ReportDataIncluded](docs/models/ReportDataIncluded.md)
 - [ReportResponse](docs/models/ReportResponse.md)
 - [StopLimitRequest](docs/models/StopLimitRequest.md)
 - [StopRequest](docs/models/StopRequest.md)
 - [Tax](docs/models/Tax.md)
 - [TimeEvent](docs/models/TimeEvent.md)
 - [TradeableInstrument](docs/models/TradeableInstrument.md)
 - [WorkingSchedule](docs/models/WorkingSchedule.md)

## Documentation For Authorization

Authentication schemes defined for the API:
<a id="apiKeyHeader"></a>
### apiKeyHeader

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author
- Ahsan Ahmed





## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in trading212_api_client.apis and trading212_api_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from trading212_api_client.apis.default_api import DefaultApi`
- `from trading212_api_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import trading212_api_client
from trading212_api_client.apis import *
from trading212_api_client.models import *
```


## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added

