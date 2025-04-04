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

from trading212_api_client import schemas  # noqa: F401


class AccountBucketResultResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            cash = schemas.NumberSchema
        
            @staticmethod
            def dividendDetails() -> typing.Type['DividendDetails']:
                return DividendDetails
            id = schemas.Int64Schema
            progress = schemas.NumberSchema
        
            @staticmethod
            def result() -> typing.Type['InvestmentResult']:
                return InvestmentResult
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AHEAD(cls):
                    return cls("AHEAD")
                
                @schemas.classproperty
                def ON_TRACK(cls):
                    return cls("ON_TRACK")
                
                @schemas.classproperty
                def BEHIND(cls):
                    return cls("BEHIND")
            __annotations__ = {
                "cash": cash,
                "dividendDetails": dividendDetails,
                "id": id,
                "progress": progress,
                "result": result,
                "status": status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cash"]) -> MetaOapg.properties.cash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dividendDetails"]) -> 'DividendDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["progress"]) -> MetaOapg.properties.progress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> 'InvestmentResult': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cash", "dividendDetails", "id", "progress", "result", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cash"]) -> typing.Union[MetaOapg.properties.cash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dividendDetails"]) -> typing.Union['DividendDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["progress"]) -> typing.Union[MetaOapg.properties.progress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> typing.Union['InvestmentResult', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cash", "dividendDetails", "id", "progress", "result", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        cash: typing.Union[MetaOapg.properties.cash, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        dividendDetails: typing.Union['DividendDetails', schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        progress: typing.Union[MetaOapg.properties.progress, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        result: typing.Union['InvestmentResult', schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccountBucketResultResponse':
        return super().__new__(
            cls,
            *_args,
            cash=cash,
            dividendDetails=dividendDetails,
            id=id,
            progress=progress,
            result=result,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from trading212_api_client.model.dividend_details import DividendDetails
from trading212_api_client.model.investment_result import InvestmentResult
