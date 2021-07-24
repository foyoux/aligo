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

    # def __post_init__(self):
    #     self.privileges = _null_list(Privilege, self.privileges)
