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


class DividendDetails(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            gained = schemas.NumberSchema
            inCash = schemas.NumberSchema
            reinvested = schemas.NumberSchema
            __annotations__ = {
                "gained": gained,
                "inCash": inCash,
                "reinvested": reinvested,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gained"]) -> MetaOapg.properties.gained: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inCash"]) -> MetaOapg.properties.inCash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reinvested"]) -> MetaOapg.properties.reinvested: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["gained", "inCash", "reinvested", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gained"]) -> typing.Union[MetaOapg.properties.gained, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inCash"]) -> typing.Union[MetaOapg.properties.inCash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reinvested"]) -> typing.Union[MetaOapg.properties.reinvested, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gained", "inCash", "reinvested", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        gained: typing.Union[MetaOapg.properties.gained, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        inCash: typing.Union[MetaOapg.properties.inCash, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        reinvested: typing.Union[MetaOapg.properties.reinvested, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DividendDetails':
        return super().__new__(
            cls,
            *_args,
            gained=gained,
            inCash=inCash,
            reinvested=reinvested,
            _configuration=_configuration,
            **kwargs,
        )
