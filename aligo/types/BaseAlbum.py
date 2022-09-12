"""..."""
from dataclasses import dataclass, field
from typing import List

from .BaseFile import BaseFile
from .DataClass import DataClass


@dataclass
class _BaseAlbumList(DataClass):
    """..."""
    list: List[BaseFile] = field(default_factory=list)


@dataclass
class BaseAlbum(DataClass):
    """..."""
    owner: str = None
    name: str = None
    description: str = None
    album_id: str = None
    file_count: int = None
    image_count: int = None
    video_count: int = None
    created_at: int = None
    updated_at: int = None
    cover: _BaseAlbumList = None
