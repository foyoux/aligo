"""批量响应"""

from dataclasses import dataclass

from aligo.types import *


@dataclass
class BatchResponse(DataClass):
    """..."""
    id: str = None
    status: int = None
    body: BaseFile = None
    method: str = None
