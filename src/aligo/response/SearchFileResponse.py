"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DatClass, BaseFile


@dataclass
class SearchFileResponse(DatClass):
    """..."""
    items: List[BaseFile] = field(default_factory=list)
    next_marker: str = ''
    punished_file_count: int = 0
