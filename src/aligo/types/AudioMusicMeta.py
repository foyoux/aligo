"""..."""
from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class AudioMusicMeta(DataClass):
    """..."""
    title: str = None
    artist: str = None
    album: str = None
    cover_url: str = None
