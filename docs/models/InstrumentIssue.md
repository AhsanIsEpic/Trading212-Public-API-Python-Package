# trading212_api_client.model.instrument_issue.InstrumentIssue

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] must be one of ["DELISTED", "SUSPENDED", "NO_LONGER_TRADABLE", "MAX_POSITION_SIZE_REACHED", "APPROACHING_MAX_POSITION_SIZE", "COMPLEX_INSTRUMENT_APP_TEST_REQUIRED", ] 
**severity** | str,  | str,  |  | [optional] must be one of ["IRREVERSIBLE", "REVERSIBLE", "INFORMATIVE", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

