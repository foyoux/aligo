"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import *


@dataclass
class SearchShareFileResponse(DataClass):
    """..."""
    items: List[BaseShareFile] = field(default_factory=list)
    next_marker: str = ''
    punished_file_count: int = 0
