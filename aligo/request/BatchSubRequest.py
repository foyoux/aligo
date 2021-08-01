"""..."""
from dataclasses import dataclass
from typing import Dict

from aligo.types import DataClass
from aligo.types.DataClass import DataType


@dataclass
class BatchSubRequest(DataClass):
    """..."""
    body: DataType
    id: str
    url: str
    headers: Dict = None
    method: str = 'POST'

    def __post_init__(self):
        self.headers = {"Content-Type": "application/json"}
        super(BatchSubRequest, self).__post_init__()
