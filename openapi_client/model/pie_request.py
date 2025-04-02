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


class PieRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class dividendCashAction(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "REINVEST": "REINVEST",
                        "TO_ACCOUNT_CASH": "TO_ACCOUNT_CASH",
                    }
                
                @schemas.classproperty
                def REINVEST(cls):
                    return cls("REINVEST")
                
                @schemas.classproperty
                def TO_ACCOUNT_CASH(cls):
                    return cls("TO_ACCOUNT_CASH")
            endDate = schemas.DateTimeSchema
            goal = schemas.NumberSchema
            icon = schemas.StrSchema
            
            
            class instrumentShares(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.NumberSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, decimal.Decimal, int, float, ],
                ) -> 'instrumentShares':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            name = schemas.StrSchema
            __annotations__ = {
                "dividendCashAction": dividendCashAction,
                "endDate": endDate,
                "goal": goal,
                "icon": icon,
                "instrumentShares": instrumentShares,
                "name": name,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dividendCashAction"]) -> MetaOapg.properties.dividendCashAction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goal"]) -> MetaOapg.properties.goal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instrumentShares"]) -> MetaOapg.properties.instrumentShares: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dividendCashAction", "endDate", "goal", "icon", "instrumentShares", "name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dividendCashAction"]) -> typing.Union[MetaOapg.properties.dividendCashAction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goal"]) -> typing.Union[MetaOapg.properties.goal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> typing.Union[MetaOapg.properties.icon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instrumentShares"]) -> typing.Union[MetaOapg.properties.instrumentShares, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dividendCashAction", "endDate", "goal", "icon", "instrumentShares", "name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        dividendCashAction: typing.Union[MetaOapg.properties.dividendCashAction, str, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, datetime, schemas.Unset] = schemas.unset,
        goal: typing.Union[MetaOapg.properties.goal, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        icon: typing.Union[MetaOapg.properties.icon, str, schemas.Unset] = schemas.unset,
        instrumentShares: typing.Union[MetaOapg.properties.instrumentShares, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PieRequest':
        return super().__new__(
            cls,
            *_args,
            dividendCashAction=dividendCashAction,
            endDate=endDate,
            goal=goal,
            icon=icon,
            instrumentShares=instrumentShares,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )
