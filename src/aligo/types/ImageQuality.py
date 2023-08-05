"""..."""
from dataclasses import dataclass

from .Type import DatClass


@dataclass
class ImageQuality(DatClass):
    """..."""
    clarity: int = None
    clarity_score: int = None
    color: int = None
    color_score: int = None
    composition_score: int = None
    contrast: int = None
    contrast_score: int = None
    exposure: int = None
    exposure_score: int = None
    overall_score: int = None
