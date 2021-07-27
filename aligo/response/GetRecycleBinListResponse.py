"""..."""
from dataclasses import dataclass
from typing import List

from aligo.types import BaseFile
from aligo.types import DataClass


@dataclass
class GetRecycleBinListResponse(DataClass):
    """..."""
    items: List[BaseFile]
    next_marker: str = ''
