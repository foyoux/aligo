"""..."""
from dataclasses import dataclass
from typing import List

from .DataClass import DataClass
from .Privilege import Privilege


@dataclass
class PersonalRightsInfo(DataClass):
    """..."""
    spu_id: str = None
    name: str = None
    is_expires: bool = None
    privileges: List[Privilege] = None
