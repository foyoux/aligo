"""..."""
from dataclasses import dataclass

from datclass import DatClass

from aligo.types.Enum import *


@dataclass
class ShareItemInfo(DatClass):
    """..."""
    category: BaseFileCategory = None
    file_extension: str = None
    file_id: str = None
    file_name: str = None
    thumbnail: str = None
    type: BaseFileType = None
