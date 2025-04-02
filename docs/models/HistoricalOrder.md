# trading212_api_client.model.historical_order.HistoricalOrder

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dateCreated** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**dateExecuted** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**dateModified** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**executor** | str,  | str,  |  | [optional] must be one of ["API", "IOS", "ANDROID", "WEB", "SYSTEM", "AUTOINVEST", ] 
**fillCost** | decimal.Decimal, int, float,  | decimal.Decimal,  | In the instrument currency | [optional] 
**fillId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**fillPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | In the instrument currency | [optional] 
**fillResult** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**fillType** | str,  | str,  |  | [optional] must be one of ["TOTV", "OTC", ] 
**filledQuantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | Applicable to quantity orders | [optional] 
**filledValue** | decimal.Decimal, int, float,  | decimal.Decimal,  | Applicable to value orders | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**limitPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | Applicable to limit orders | [optional] 
**orderedQuantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | Applicable to quantity orders | [optional] 
**orderedValue** | decimal.Decimal, int, float,  | decimal.Decimal,  | Applicable to value orders | [optional] 
**parentOrder** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**status** | str,  | str,  |  | [optional] must be one of ["LOCAL", "UNCONFIRMED", "CONFIRMED", "NEW", "CANCELLING", "CANCELLED", "PARTIALLY_FILLED", "FILLED", "REJECTED", "REPLACING", "REPLACED", ] 
**stopPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | Applicable to stop orders | [optional] 
**[taxes](#taxes)** | list, tuple,  | tuple,  |  | [optional] 
**ticker** | str,  | str,  |  | [optional] 
**timeValidity** | str,  | str,  | Applicable to stop, limit and stopLimit orders | [optional] must be one of ["DAY", "GOOD_TILL_CANCEL", ] 
**type** | str,  | str,  |  | [optional] must be one of ["LIMIT", "STOP", "MARKET", "STOP_LIMIT", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# taxes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Tax**](Tax.md) | [**Tax**](Tax.md) | [**Tax**](Tax.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

