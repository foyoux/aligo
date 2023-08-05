"""..."""

from dataclasses import dataclass

from .CroppingBoundary import CroppingBoundary
from .Type import DatClass


@dataclass
class CroppingSuggestionItem(DatClass):
    """..."""
    aspect_ratio: str = None
    cropping_boundary: CroppingBoundary = None
    score: int = None
