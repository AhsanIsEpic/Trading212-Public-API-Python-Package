# trading212_api_client.model.position.Position

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**averagePrice** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**currentPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**frontend** | str,  | str,  | Origin | [optional] must be one of ["API", "IOS", "ANDROID", "WEB", "SYSTEM", "AUTOINVEST", ] 
**fxPpl** | decimal.Decimal, int, float,  | decimal.Decimal,  | Forex movement impact, only applies to positions with instrument currency that differs from the accounts&#x27; | [optional] 
**initialFillDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**maxBuy** | decimal.Decimal, int, float,  | decimal.Decimal,  | Additional quantity that can be bought | [optional] 
**maxSell** | decimal.Decimal, int, float,  | decimal.Decimal,  | Quantity that can be sold | [optional] 
**pieQuantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | Invested in pies | [optional] 
**ppl** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**ticker** | str,  | str,  | Unique instrument identifier | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

