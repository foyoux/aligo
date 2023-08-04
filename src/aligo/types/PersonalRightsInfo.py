"""..."""
from dataclasses import dataclass
from typing import List

from datclass import DatClass

from .Privilege import Privilege


@dataclass
class PersonalRightsInfo(DatClass):
    """..."""
    spu_id: str = None
    name: str = None
    is_expires: bool = None
    privileges: List[Privilege] = None
