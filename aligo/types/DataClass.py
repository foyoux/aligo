"""..."""
from dataclasses import dataclass, is_dataclass
from typing import get_type_hints, get_args, get_origin, TypeVar, Generic, Optional, List, Dict, Type


@dataclass
class DataClass:
    """..."""

    def __post_init__(self):
        """
        Unified instantiation of attributes through type hints to avoid repeated implementation of the __post_init__ method
        So type hints is necessary
        :return:
        """
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

        # Object of type UploadPartInfo is not JSON serializable
        # super(DataClass, self).__init__(**self.__dict__)


DataType = TypeVar('DataType', DataClass, DataClass, covariant=True)


def _null_list(cls: Generic[DataType], may_null: Optional[List[DataType]]) -> List[DataType]:
    # 'NoneType' object is not iterable
    if may_null and len(may_null) != 0:
        if isinstance(may_null[0], dict):
            return [cls(**i) for i in may_null]
        else:
            # return [cls(**i.__dict__) for i in may_null]
            return may_null
    else:
        return []


def _null_dict(cls: Type[DataType], may_null: Optional[Dict]) -> DataType:
    if may_null is None:
        # may_null = {}  # 统一代码调用
        return None  # 后面发现, 这样浪费内存, 有些东西完全是None, 却暂用很多对象
    if isinstance(may_null, dict):
        return cls(**may_null)
    # return cls(**may_null.__dict__)
    return may_null  # type: ignore
