"""..."""
from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class ImageTag(DataClass):
    """..."""
    name: str = None
    parent_name: str = None
    confidence: int = None
    tag_level: int = None
    selected: bool = None
    centric_score: int = None
