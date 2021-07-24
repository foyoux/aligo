"""..."""
from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class VideoMediaAudioStream(DataClass):
    """..."""
    code_name: str = None
    duration: str = None
    bit_rate: str = None
    channel_layout: str = None
    channels: int = None
    sample_rate: str = None
