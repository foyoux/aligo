"""..."""
from dataclasses import dataclass
from typing import Dict

from aligo.types import DataClass


@dataclass
class BatchSubRequest(DataClass):
    """..."""
    body: Dict
    headers: Dict
    id: str
    url: str
    method: str = 'POST'
