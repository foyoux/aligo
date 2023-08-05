"""..."""
from dataclasses import dataclass

from .Type import DatClass


@dataclass
class CroppingBoundary(DatClass):
    """..."""
    height: int = None
    left: int = None
    top: int = None
    width: int = None
