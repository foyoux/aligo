"""..."""
from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class VideoMediaVideoStream(DataClass):
    """..."""
    code_name: str = None
    fps: str = None
    bitrate: str = None
    clarity: str = None
    duration: str = None
