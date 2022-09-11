"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass, BaseAlbum


@dataclass
class AlbumListResponse(DataClass):
    """..."""
    items: List[BaseAlbum] = field(default_factory=list, repr=False)
    next_marker: str = ''
    album_count: int = None
