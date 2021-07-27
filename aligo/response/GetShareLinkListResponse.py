"""..."""
from dataclasses import dataclass
from typing import List

from aligo.types import DataClass, ShareLinkSchema


@dataclass
class GetShareLinkListResponse(DataClass):
    """..."""
    items: List[ShareLinkSchema]
    next_marker: str = ''
