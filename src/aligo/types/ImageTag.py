"""..."""
from dataclasses import dataclass

from .Type import DatClass


@dataclass
class ImageTag(DatClass):
    """..."""
    name: str = None
    parent_name: str = None
    confidence: int = None
    tag_level: int = None
    selected: bool = None
    centric_score: int = None
