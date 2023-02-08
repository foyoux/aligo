"""..."""
from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class VideoPreviewSprite(DataClass):
    """..."""
    col: int = None
    count: int = None
    frame_count: int = None
    frame_height: int = None
    frame_width: int = None
    row: int = None
    status: str = None
