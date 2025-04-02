# coding: utf-8

"""
    Trading212 Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api_v0_equity_portfolio.get import Portfolio
from openapi_client.paths.api_v0_equity_portfolio_ticker.get import PositionByTicker
from openapi_client.paths.api_v0_equity_portfolio_ticker.post import PositionByTickerV2


class PersonalPortfolioApi(
    Portfolio,
    PositionByTicker,
    PositionByTickerV2,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
