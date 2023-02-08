"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import *


@dataclass
class SearchFileResponse(DataClass):
    """..."""
    items: List[BaseFile] = field(default_factory=list)
    next_marker: str = ''
    punished_file_count: int = 0
