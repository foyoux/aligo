"""批量响应"""
from dataclasses import dataclass
from typing import Generic

from datclass import DatClass

from aligo.types import DataType


@dataclass
class BatchSubResponse(DatClass, Generic[DataType]):
    """..."""
    id: str = None
    status: int = None
    body: DataType = None
    method: str = None
