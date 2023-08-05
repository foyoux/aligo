"""..."""
from dataclasses import dataclass

from .Type import DatClass


@dataclass
class VideoMediaVideoStream(DatClass):
    """..."""
    code_name: str = None
    fps: str = None
    bitrate: str = None
    clarity: str = None
    duration: str = None
