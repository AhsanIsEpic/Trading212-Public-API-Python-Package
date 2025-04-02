# trading212_api_client.model.tax.Tax

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**fillId** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] must be one of ["COMMISSION_TURNOVER", "CURRENCY_CONVERSION_FEE", "FINRA_FEE", "FRENCH_TRANSACTION_TAX", "PTM_LEVY", "STAMP_DUTY", "STAMP_DUTY_RESERVE_TAX", "TRANSACTION_FEE", ] 
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**timeCharged** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

