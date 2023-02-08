"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass, ListAlbumItem


@dataclass
class AlbumListResponse(DataClass):
    """..."""
    items: List[ListAlbumItem] = field(default_factory=list, repr=False)
    next_marker: str = ''
    album_count: int = None
