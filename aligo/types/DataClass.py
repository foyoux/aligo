"""..."""
from dataclasses import dataclass, is_dataclass
from typing import get_type_hints, get_args, get_origin, TypeVar, Generic, Optional, List, Dict, Type

DataType = TypeVar('DataType')


@dataclass
class DataClass:
    """..."""

    def __post_init__(self):
        """序列化属性"""
        hints = get_type_hints(self)
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
            return [cls(**i) for i in may_null]
        else:
            return may_null
    else:
        return []


def _null_dict(cls: Type[DataType], may_null: Optional[Dict]) -> DataType:
    if may_null is None:
        return None
    if isinstance(may_null, dict):
        return cls(**may_null)
    return may_null
