"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass, BaseFile


@dataclass
class GetFileListResponse(DataClass):
    """..."""
    items: List[BaseFile]
    next_marker: str = field(default='', repr=False)
