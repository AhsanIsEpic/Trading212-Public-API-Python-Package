import typing_extensions

from trading212_api_client.apis.tags import TagValues
from trading212_api_client.apis.tags.instruments_metadata_api import InstrumentsMetadataApi
from trading212_api_client.apis.tags.pies_api import PiesApi
from trading212_api_client.apis.tags.equity_orders_api import EquityOrdersApi
from trading212_api_client.apis.tags.account_data_api import AccountDataApi
from trading212_api_client.apis.tags.personal_portfolio_api import PersonalPortfolioApi
from trading212_api_client.apis.tags.historical_items_api import HistoricalItemsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.INSTRUMENTS_METADATA: InstrumentsMetadataApi,
        TagValues.PIES: PiesApi,
        TagValues.EQUITY_ORDERS: EquityOrdersApi,
        TagValues.ACCOUNT_DATA: AccountDataApi,
        TagValues.PERSONAL_PORTFOLIO: PersonalPortfolioApi,
        TagValues.HISTORICAL_ITEMS: HistoricalItemsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.INSTRUMENTS_METADATA: InstrumentsMetadataApi,
        TagValues.PIES: PiesApi,
        TagValues.EQUITY_ORDERS: EquityOrdersApi,
        TagValues.ACCOUNT_DATA: AccountDataApi,
        TagValues.PERSONAL_PORTFOLIO: PersonalPortfolioApi,
        TagValues.HISTORICAL_ITEMS: HistoricalItemsApi,
    }
)
