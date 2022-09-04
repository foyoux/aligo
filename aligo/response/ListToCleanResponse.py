"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import BaseFile
from aligo.types import DataClass


@dataclass
class ListToCleanResponse(DataClass):
    """..."""
    items: List[BaseFile] = field(default_factory=list)
    next_marker: str = ''
