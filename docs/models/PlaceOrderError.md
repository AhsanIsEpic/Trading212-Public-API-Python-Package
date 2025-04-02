# openapi_client.model.place_order_error.PlaceOrderError

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clarification** | str,  | str,  |  | [optional] 
**code** | str,  | str,  |  | [optional] must be one of ["SellingEquityNotOwned", "CantLegalyTradeException", "InsufficientResources", "InsufficientValueForStocksSell", "TargetPriceTooFar", "TargetPriceTooClose", "NotEligibleForISA", "ShareLendingAgreementNotAccepted", "InstrumentNotFound", "MaxEquityBuyQuantityExceeded", "MaxEquitySellQuantityExceeded", "LimitPriceMissing", "StopPriceMissing", "TickerMissing", "QuantityMissing", "MaxQuantityExceeded", "InvalidValue", "InsufficientFreeForStocksException", "MinValueExceeded", "MinQuantityExceeded", "PriceTooFar", "UNDEFINED", "NotAvailableForRealMoneyAccounts", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

