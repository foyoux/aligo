"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import BaseFile
from aligo.types import DataClass


@dataclass
class ListResponse(DataClass):
    """..."""
    items: List[BaseFile]
    next_marker: str = field(default='', repr=False)
