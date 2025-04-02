import typing_extensions

from trading212_api_client.paths import PathValues
from trading212_api_client.apis.paths.api_v0_equity_account_cash import ApiV0EquityAccountCash
from trading212_api_client.apis.paths.api_v0_equity_account_info import ApiV0EquityAccountInfo
from trading212_api_client.apis.paths.api_v0_equity_history_orders import ApiV0EquityHistoryOrders
from trading212_api_client.apis.paths.api_v0_equity_metadata_exchanges import ApiV0EquityMetadataExchanges
from trading212_api_client.apis.paths.api_v0_equity_metadata_instruments import ApiV0EquityMetadataInstruments
from trading212_api_client.apis.paths.api_v0_equity_orders import ApiV0EquityOrders
from trading212_api_client.apis.paths.api_v0_equity_orders_limit import ApiV0EquityOrdersLimit
from trading212_api_client.apis.paths.api_v0_equity_orders_market import ApiV0EquityOrdersMarket
from trading212_api_client.apis.paths.api_v0_equity_orders_stop import ApiV0EquityOrdersStop
from trading212_api_client.apis.paths.api_v0_equity_orders_stop_limit import ApiV0EquityOrdersStopLimit
from trading212_api_client.apis.paths.api_v0_equity_orders_id import ApiV0EquityOrdersId
from trading212_api_client.apis.paths.api_v0_equity_pies import ApiV0EquityPies
from trading212_api_client.apis.paths.api_v0_equity_pies_id import ApiV0EquityPiesId
from trading212_api_client.apis.paths.api_v0_equity_pies_id_duplicate import ApiV0EquityPiesIdDuplicate
from trading212_api_client.apis.paths.api_v0_equity_portfolio import ApiV0EquityPortfolio
from trading212_api_client.apis.paths.api_v0_equity_portfolio_ticker import ApiV0EquityPortfolioTicker
from trading212_api_client.apis.paths.api_v0_history_dividends import ApiV0HistoryDividends
from trading212_api_client.apis.paths.api_v0_history_exports import ApiV0HistoryExports
from trading212_api_client.apis.paths.api_v0_history_transactions import ApiV0HistoryTransactions

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V0_EQUITY_ACCOUNT_CASH: ApiV0EquityAccountCash,
        PathValues.API_V0_EQUITY_ACCOUNT_INFO: ApiV0EquityAccountInfo,
        PathValues.API_V0_EQUITY_HISTORY_ORDERS: ApiV0EquityHistoryOrders,
        PathValues.API_V0_EQUITY_METADATA_EXCHANGES: ApiV0EquityMetadataExchanges,
        PathValues.API_V0_EQUITY_METADATA_INSTRUMENTS: ApiV0EquityMetadataInstruments,
        PathValues.API_V0_EQUITY_ORDERS: ApiV0EquityOrders,
        PathValues.API_V0_EQUITY_ORDERS_LIMIT: ApiV0EquityOrdersLimit,
        PathValues.API_V0_EQUITY_ORDERS_MARKET: ApiV0EquityOrdersMarket,
        PathValues.API_V0_EQUITY_ORDERS_STOP: ApiV0EquityOrdersStop,
        PathValues.API_V0_EQUITY_ORDERS_STOP_LIMIT: ApiV0EquityOrdersStopLimit,
        PathValues.API_V0_EQUITY_ORDERS_ID: ApiV0EquityOrdersId,
        PathValues.API_V0_EQUITY_PIES: ApiV0EquityPies,
        PathValues.API_V0_EQUITY_PIES_ID: ApiV0EquityPiesId,
        PathValues.API_V0_EQUITY_PIES_ID_DUPLICATE: ApiV0EquityPiesIdDuplicate,
        PathValues.API_V0_EQUITY_PORTFOLIO: ApiV0EquityPortfolio,
        PathValues.API_V0_EQUITY_PORTFOLIO_TICKER: ApiV0EquityPortfolioTicker,
        PathValues.API_V0_HISTORY_DIVIDENDS: ApiV0HistoryDividends,
        PathValues.API_V0_HISTORY_EXPORTS: ApiV0HistoryExports,
        PathValues.API_V0_HISTORY_TRANSACTIONS: ApiV0HistoryTransactions,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V0_EQUITY_ACCOUNT_CASH: ApiV0EquityAccountCash,
        PathValues.API_V0_EQUITY_ACCOUNT_INFO: ApiV0EquityAccountInfo,
        PathValues.API_V0_EQUITY_HISTORY_ORDERS: ApiV0EquityHistoryOrders,
        PathValues.API_V0_EQUITY_METADATA_EXCHANGES: ApiV0EquityMetadataExchanges,
        PathValues.API_V0_EQUITY_METADATA_INSTRUMENTS: ApiV0EquityMetadataInstruments,
        PathValues.API_V0_EQUITY_ORDERS: ApiV0EquityOrders,
        PathValues.API_V0_EQUITY_ORDERS_LIMIT: ApiV0EquityOrdersLimit,
        PathValues.API_V0_EQUITY_ORDERS_MARKET: ApiV0EquityOrdersMarket,
        PathValues.API_V0_EQUITY_ORDERS_STOP: ApiV0EquityOrdersStop,
        PathValues.API_V0_EQUITY_ORDERS_STOP_LIMIT: ApiV0EquityOrdersStopLimit,
        PathValues.API_V0_EQUITY_ORDERS_ID: ApiV0EquityOrdersId,
        PathValues.API_V0_EQUITY_PIES: ApiV0EquityPies,
        PathValues.API_V0_EQUITY_PIES_ID: ApiV0EquityPiesId,
        PathValues.API_V0_EQUITY_PIES_ID_DUPLICATE: ApiV0EquityPiesIdDuplicate,
        PathValues.API_V0_EQUITY_PORTFOLIO: ApiV0EquityPortfolio,
        PathValues.API_V0_EQUITY_PORTFOLIO_TICKER: ApiV0EquityPortfolioTicker,
        PathValues.API_V0_HISTORY_DIVIDENDS: ApiV0HistoryDividends,
        PathValues.API_V0_HISTORY_EXPORTS: ApiV0HistoryExports,
        PathValues.API_V0_HISTORY_TRANSACTIONS: ApiV0HistoryTransactions,
    }
)
