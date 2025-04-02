# trading212_api_client.model.account_bucket_result_response.AccountBucketResultResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cash** | decimal.Decimal, int, float,  | decimal.Decimal,  | Amount of money put into the pie in account currency | [optional] 
**dividendDetails** | [**DividendDetails**](DividendDetails.md) | [**DividendDetails**](DividendDetails.md) |  | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**progress** | decimal.Decimal, int, float,  | decimal.Decimal,  | Progress of the pie based on the set goal | [optional] 
**result** | [**InvestmentResult**](InvestmentResult.md) | [**InvestmentResult**](InvestmentResult.md) |  | [optional] 
**status** | str,  | str,  | Status of the pie based on the set goal | [optional] must be one of ["AHEAD", "ON_TRACK", "BEHIND", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

