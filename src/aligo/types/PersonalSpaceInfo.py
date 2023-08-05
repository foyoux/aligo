"""..."""
from dataclasses import dataclass

from .Type import DatClass


@dataclass
class PersonalSpaceInfo(DatClass):
    """..."""
    used_size: int = None
    total_size: int = None
