"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DatClass, ShareLinkSchema


@dataclass
class GetShareLinkListResponse(DatClass):
    """..."""
    items: List[ShareLinkSchema] = field(default_factory=list)
    next_marker: str = ''
    punished_file_count: int = 0
