"""..."""
from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class RateLimit(DataClass):
    """..."""
    part_size: int = None
    part_speed: int = None
