"""..."""

from dataclasses import dataclass

from datclass import DatClass

from .CroppingBoundary import CroppingBoundary


@dataclass
class CroppingSuggestionItem(DatClass):
    """..."""
    aspect_ratio: str = None
    cropping_boundary: CroppingBoundary = None
    score: int = None
