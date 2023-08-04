"""..."""
from dataclasses import dataclass, field
from typing import List

from datclass import DatClass

from aligo.types import BaseFile


@dataclass
class AimSearchResponse(DatClass):
    """..."""
    items: List[BaseFile] = field(default_factory=list)
    next_marker: str = ''
    total_count: int = None
    punished_file_count: int = 0
