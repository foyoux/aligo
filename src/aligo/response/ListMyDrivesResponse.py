"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DatClass, BaseDrive


@dataclass
class ListMyDrivesResponse(DatClass):
    """..."""
    items: List[BaseDrive] = field(default_factory=list)
    next_marker: str = ''
