"""..."""
from dataclasses import dataclass

from .DataClass import DataClass


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
