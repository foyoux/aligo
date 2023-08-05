"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DatClass
from .BatchSubRequest import BatchSubRequest


@dataclass
class BatchRequest(DatClass):
    """..."""
    requests: List[BatchSubRequest] = field(default_factory=list)
    resource: str = 'file'
