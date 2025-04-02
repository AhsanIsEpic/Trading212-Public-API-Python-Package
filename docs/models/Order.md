# trading212_api_client.model.order.Order

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**creationTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**filledQuantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | Applicable to quantity orders | [optional] 
**filledValue** | decimal.Decimal, int, float,  | decimal.Decimal,  | Applicable to value orders | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**limitPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | Applicable to LIMIT and STOP_LIMIT orders | [optional] 
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | Applicable to quantity orders | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["LOCAL", "UNCONFIRMED", "CONFIRMED", "NEW", "CANCELLING", "CANCELLED", "PARTIALLY_FILLED", "FILLED", "REJECTED", "REPLACING", "REPLACED", ] 
**stopPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | Applicable to STOP and STOP_LIMIT orders | [optional] 
**strategy** | str,  | str,  |  | [optional] must be one of ["QUANTITY", "VALUE", ] 
**ticker** | str,  | str,  | Unique instrument identifier. Get from the /instruments endpoint | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["LIMIT", "STOP", "MARKET", "STOP_LIMIT", ] 
**value** | decimal.Decimal, int, float,  | decimal.Decimal,  | Applicable to value orders | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

