"""..."""
from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class CroppingBoundary(DataClass):
    """..."""
    height: int = None
    left: int = None
    top: int = None
    width: int = None
