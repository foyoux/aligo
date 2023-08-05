"""..."""
from dataclasses import dataclass

from .Type import DatClass


@dataclass
class AudioMusicMeta(DatClass):
    """..."""
    title: str = None
    artist: str = None
    album: str = None
    cover_url: str = None
