"""..."""
from dataclasses import dataclass, field
from typing import List

from .BaseFile import BaseFile
from .DataClass import DataClass


@dataclass
class ListAlbumItem(DataClass):
    """..."""
    name: str = None
    type: str = None
    album_id: int = None
    total_count: int = None
    file_list: List[BaseFile] = field(default_factory=list)
