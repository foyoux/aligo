"""..."""
from dataclasses import dataclass
from dataclasses import field
from typing import List

from .BaseFile import BaseFile
from .Type import DatClass


@dataclass
class ListAlbumItem(DatClass):
    """..."""
    name: str = None
    type: str = None
    album_id: int = None
    total_count: int = None
    file_list: List[BaseFile] = field(default_factory=list)
