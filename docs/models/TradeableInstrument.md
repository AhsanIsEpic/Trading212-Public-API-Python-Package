# openapi_client.model.tradeable_instrument.TradeableInstrument

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**addedOn** | str, datetime,  | str,  | On the platform since | [optional] value must conform to RFC-3339 date-time
**currencyCode** | str,  | str,  | ISO 4217 | [optional] 
**isin** | str,  | str,  |  | [optional] 
**maxOpenQuantity** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**minTradeQuantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | A single order must be equal to or exceed this value | [optional] 
**name** | str,  | str,  |  | [optional] 
**shortName** | str,  | str,  |  | [optional] 
**ticker** | str,  | str,  | Unique identifier | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["CRYPTOCURRENCY", "ETF", "FOREX", "FUTURES", "INDEX", "STOCK", "WARRANT", "CRYPTO", "CVR", "CORPACT", ] 
**workingScheduleId** | decimal.Decimal, int,  | decimal.Decimal,  | Get items in the /exchanges endpoint | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

