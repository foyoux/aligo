"""..."""
from dataclasses import dataclass

from .Type import DatClass


@dataclass
class SystemTag(DatClass):
    """..."""
    name: str = None
    en_name: str = None
    confidence: int = None
    parent_en_name: str = None
    parent_name: str = None
    selected: bool = None
    tag_level: int = None
    centric_score: int = None
