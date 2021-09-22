"""GetFilePathResponse"""
from dataclasses import dataclass, field
from typing import List

from aligo.types import *


@dataclass
class GetFilePathResponse(DataClass):
    """GetFilePathResponse"""
    items: List[BaseFile] = field(default_factory=list)
