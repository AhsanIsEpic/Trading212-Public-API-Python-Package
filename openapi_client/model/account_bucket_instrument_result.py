# coding: utf-8

"""
    Trading212 Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class AccountBucketInstrumentResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            currentShare = schemas.NumberSchema
            expectedShare = schemas.NumberSchema
            
            
            class issues(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    
                    @staticmethod
                    def items() -> typing.Type['InstrumentIssue']:
                        return InstrumentIssue
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['InstrumentIssue'], typing.List['InstrumentIssue']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'issues':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'InstrumentIssue':
                    return super().__getitem__(i)
            ownedQuantity = schemas.NumberSchema
        
            @staticmethod
            def result() -> typing.Type['InvestmentResult']:
                return InvestmentResult
            ticker = schemas.StrSchema
            __annotations__ = {
                "currentShare": currentShare,
                "expectedShare": expectedShare,
                "issues": issues,
                "ownedQuantity": ownedQuantity,
                "result": result,
                "ticker": ticker,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentShare"]) -> MetaOapg.properties.currentShare: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expectedShare"]) -> MetaOapg.properties.expectedShare: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issues"]) -> MetaOapg.properties.issues: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownedQuantity"]) -> MetaOapg.properties.ownedQuantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> 'InvestmentResult': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ticker"]) -> MetaOapg.properties.ticker: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["currentShare", "expectedShare", "issues", "ownedQuantity", "result", "ticker", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentShare"]) -> typing.Union[MetaOapg.properties.currentShare, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expectedShare"]) -> typing.Union[MetaOapg.properties.expectedShare, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issues"]) -> typing.Union[MetaOapg.properties.issues, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownedQuantity"]) -> typing.Union[MetaOapg.properties.ownedQuantity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> typing.Union['InvestmentResult', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ticker"]) -> typing.Union[MetaOapg.properties.ticker, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currentShare", "expectedShare", "issues", "ownedQuantity", "result", "ticker", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        currentShare: typing.Union[MetaOapg.properties.currentShare, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        expectedShare: typing.Union[MetaOapg.properties.expectedShare, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        issues: typing.Union[MetaOapg.properties.issues, list, tuple, schemas.Unset] = schemas.unset,
        ownedQuantity: typing.Union[MetaOapg.properties.ownedQuantity, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        result: typing.Union['InvestmentResult', schemas.Unset] = schemas.unset,
        ticker: typing.Union[MetaOapg.properties.ticker, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccountBucketInstrumentResult':
        return super().__new__(
            cls,
            *_args,
            currentShare=currentShare,
            expectedShare=expectedShare,
            issues=issues,
            ownedQuantity=ownedQuantity,
            result=result,
            ticker=ticker,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.instrument_issue import InstrumentIssue
from openapi_client.model.investment_result import InvestmentResult
