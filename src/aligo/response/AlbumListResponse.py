"""..."""
from dataclasses import dataclass, field
from typing import List

from datclass import DatClass

from aligo.types import ListAlbumItem


@dataclass
class AlbumListResponse(DatClass):
    """..."""
    items: List[ListAlbumItem] = field(default_factory=list, repr=False)
    next_marker: str = ''
    album_count: int = None
