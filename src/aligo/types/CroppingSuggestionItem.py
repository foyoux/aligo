"""..."""
from dataclasses import dataclass

from .CroppingBoundary import CroppingBoundary
from .DataClass import DataClass


@dataclass
class CroppingSuggestionItem(DataClass):
    """..."""
    aspect_ratio: str = None
    cropping_boundary: CroppingBoundary = None
    score: int = None
