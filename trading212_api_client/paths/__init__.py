# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from trading212_api_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V0_EQUITY_ACCOUNT_CASH = "/api/v0/equity/account/cash"
    API_V0_EQUITY_ACCOUNT_INFO = "/api/v0/equity/account/info"
    API_V0_EQUITY_HISTORY_ORDERS = "/api/v0/equity/history/orders"
    API_V0_EQUITY_METADATA_EXCHANGES = "/api/v0/equity/metadata/exchanges"
    API_V0_EQUITY_METADATA_INSTRUMENTS = "/api/v0/equity/metadata/instruments"
    API_V0_EQUITY_ORDERS = "/api/v0/equity/orders"
    API_V0_EQUITY_ORDERS_LIMIT = "/api/v0/equity/orders/limit"
    API_V0_EQUITY_ORDERS_MARKET = "/api/v0/equity/orders/market"
    API_V0_EQUITY_ORDERS_STOP = "/api/v0/equity/orders/stop"
    API_V0_EQUITY_ORDERS_STOP_LIMIT = "/api/v0/equity/orders/stop_limit"
    API_V0_EQUITY_ORDERS_ID = "/api/v0/equity/orders/{id}"
    API_V0_EQUITY_PIES = "/api/v0/equity/pies"
    API_V0_EQUITY_PIES_ID = "/api/v0/equity/pies/{id}"
    API_V0_EQUITY_PIES_ID_DUPLICATE = "/api/v0/equity/pies/{id}/duplicate"
    API_V0_EQUITY_PORTFOLIO = "/api/v0/equity/portfolio"
    API_V0_EQUITY_PORTFOLIO_TICKER = "/api/v0/equity/portfolio/ticker"
    API_V0_EQUITY_PORTFOLIO_TICKER = "/api/v0/equity/portfolio/{ticker}"
    API_V0_HISTORY_DIVIDENDS = "/api/v0/history/dividends"
    API_V0_HISTORY_EXPORTS = "/api/v0/history/exports"
    API_V0_HISTORY_TRANSACTIONS = "/api/v0/history/transactions"
