"""分享文件列表响应"""

from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass, BaseShareFile


@dataclass
class GetShareFileListResponse(DataClass):
    """..."""
    items: List[BaseShareFile] = field(default_factory=list)
    next_marker: str = ''
    punished_file_count: int = 0
