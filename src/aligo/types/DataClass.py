"""..."""
from __future__ import annotations

import logging
import os
from dataclasses import dataclass, is_dataclass
from typing import TypeVar, Generic, Optional, List, Dict, Type

try:
    from typing import get_type_hints, get_origin, get_args
except ImportError:
    from typing_extensions import get_type_hints, get_origin, get_args

DataType = TypeVar('DataType')

_HINTS = {}
_LOGGER = logging.getLogger('aligo')
_ALIGO_DEBUG = os.getenv('ALIGO_DEBUG')


@dataclass
class DataClass:
    """..."""

    @staticmethod
    def _get_hints(cls: Type[DataClass]):
        """..."""
        hints = _HINTS.get(cls)
        if hints:
            return hints
        hints = get_type_hints(cls)
        _HINTS[cls] = hints
        return hints

    @staticmethod
    def fill_attrs(cls: Type[DataType], obj: Dict) -> DataType:
        """..."""
        hints = DataClass._get_hints(cls)
        params = {}
        for key, value in obj.items():
            if key in hints:
                params[key] = value
            else:
                if _ALIGO_DEBUG:
                    _LOGGER.warning(
                        f'MISSING_ATTRS {cls.__module__}.{cls.__name__}({key} : {type(value).__name__} = {repr(value)[:100]})')
        return cls(**params)

    def __post_init__(self):
        """序列化属性"""
        hints = DataClass._get_hints(self.__class__)
        for k, v in hints.items():
            origin = get_origin(v)
            if origin is None:
                if is_dataclass(v):
                    setattr(self, k, _null_dict(v, getattr(self, k)))
                    continue
            for hint_type in get_args(v):
                if is_dataclass(hint_type):
                    if origin is list:
                        setattr(self, k, _null_list(hint_type, getattr(self, k)))
                    break


def _null_list(cls: Generic[DataType], may_null: Optional[List[DataType]]) -> List[DataType]:
    if may_null and len(may_null) != 0:
        if isinstance(may_null[0], dict):
            # noinspection PyProtectedMember
            return [DataClass.fill_attrs(cls, i) for i in may_null]
        else:
            return may_null
    else:
        return []


def _null_dict(cls: Type[DataType], may_null: Optional[Dict]) -> DataType:
    if may_null is None:
        return None
    if isinstance(may_null, dict):
        # noinspection PyProtectedMember
        return DataClass.fill_attrs(cls, may_null)
    return may_null
