"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class PersonalSpaceInfo(DatClass):
    """..."""
    used_size: int = None
    total_size: int = None
