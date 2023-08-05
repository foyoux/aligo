"""..."""
from dataclasses import dataclass
from typing import List

from .Privilege import Privilege
from .Type import DatClass


@dataclass
class PersonalRightsInfo(DatClass):
    """..."""
    spu_id: str = None
    name: str = None
    is_expires: bool = None
    privileges: List[Privilege] = None
