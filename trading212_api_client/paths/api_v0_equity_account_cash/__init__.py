# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from trading212_api_client.paths.api_v0_equity_account_cash import Api

from trading212_api_client.paths import PathValues

path = PathValues.API_V0_EQUITY_ACCOUNT_CASH