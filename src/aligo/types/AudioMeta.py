"""..."""
from dataclasses import dataclass

from .Type import DatClass


@dataclass
class AudioMeta(DatClass):
    """..."""
    bitrate: int = None
    duration: int = None
    sample_rate: int = None
    channels: int = None
