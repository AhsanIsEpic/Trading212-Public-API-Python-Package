# trading212_api_client.model.account_bucket_instrument_result.AccountBucketInstrumentResult

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**currentShare** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**expectedShare** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**[issues](#issues)** | list, tuple,  | tuple,  |  | [optional] 
**ownedQuantity** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**result** | [**InvestmentResult**](InvestmentResult.md) | [**InvestmentResult**](InvestmentResult.md) |  | [optional] 
**ticker** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# issues

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InstrumentIssue**](InstrumentIssue.md) | [**InstrumentIssue**](InstrumentIssue.md) | [**InstrumentIssue**](InstrumentIssue.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

