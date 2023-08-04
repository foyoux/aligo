"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class RateLimit(DatClass):
    """..."""
    part_size: int = None
    part_speed: int = None
