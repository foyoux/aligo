"""..."""
from dataclasses import dataclass
from typing import List

from aligo.types import *


@dataclass
class SearchFileResponse(DataClass):
    """..."""
    items: List[BaseFile]
    next_marker: str = ''
