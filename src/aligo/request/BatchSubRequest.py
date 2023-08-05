"""..."""
from dataclasses import dataclass
from typing import Dict, Union

from aligo.types import DatClass


@dataclass
class BatchSubRequest(DatClass):
    """..."""
    body: Union[DatClass, Dict]
    id: str
    url: str
    headers: Dict = None
    method: str = 'POST'

    def __post_init__(self):
        self.headers = {"Content-Type": "application/json"}
        super().__post_init__()
