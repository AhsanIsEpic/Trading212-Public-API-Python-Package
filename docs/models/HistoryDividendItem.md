# trading212_api_client.model.history_dividend_item.HistoryDividendItem

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | In account currency | [optional] 
**amountInEuro** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**grossAmountPerShare** | decimal.Decimal, int, float,  | decimal.Decimal,  | In instrument currency | [optional] 
**paidOn** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**reference** | str,  | str,  |  | [optional] 
**ticker** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

