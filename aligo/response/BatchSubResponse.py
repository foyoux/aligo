"""批量响应"""

from dataclasses import dataclass
from typing import Generic
from aligo.types import *
from aligo.types.DataClass import DataType


@dataclass
class BatchSubResponse(DataClass, Generic[DataType]):
    """..."""
    id: str = None
    status: int = None
    body: DataType = None
    method: str = None
