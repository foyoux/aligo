"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass, ShareLinkSchema


@dataclass
class GetShareLinkListResponse(DataClass):
    """..."""
    items: List[ShareLinkSchema] = field(default_factory=list)
    next_marker: str = ''
    punished_file_count: int = 0
