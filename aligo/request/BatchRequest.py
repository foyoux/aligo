"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass
from .BatchSubRequest import BatchSubRequest


@dataclass
class BatchRequest(DataClass):
    """..."""
    requests: List[BatchSubRequest] = field(default_factory=list)
    resource: str = 'file'
