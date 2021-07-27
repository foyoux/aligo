"""todo"""

from dataclasses import dataclass
from typing import List

from aligo.types import DataClass, BaseShareFile


@dataclass
class GetShareFileListResponse(DataClass):
    """..."""
    items: List[BaseShareFile]
    next_marker: str = ''
