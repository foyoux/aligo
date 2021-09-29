"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import *


@dataclass
class AimSearchResponse(DataClass):
    """..."""
    items: List[BaseFile] = field(default_factory=list)
    next_marker: str = ''
    total_count: int = None
    punished_file_count: int = 0
