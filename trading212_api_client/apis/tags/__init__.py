# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from trading212_api_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    INSTRUMENTS_METADATA = "Instruments Metadata"
    PIES = "Pies"
    EQUITY_ORDERS = "Equity Orders"
    ACCOUNT_DATA = "Account Data"
    PERSONAL_PORTFOLIO = "Personal Portfolio"
    HISTORICAL_ITEMS = "Historical items"
