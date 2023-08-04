"""..."""
from dataclasses import dataclass, field
from typing import List

from datclass import DatClass

from aligo.types import BaseDrive


@dataclass
class ListMyDrivesResponse(DatClass):
    """..."""
    items: List[BaseDrive] = field(default_factory=list)
    next_marker: str = ''
