"""..."""
from dataclasses import dataclass

from aligo.types import *
from aligo.types.Enum import *


@dataclass
class ShareItemInfo(DataClass):
    """..."""
    category: BaseFileCategory = None
    file_extension: str = None
    file_id: str = None
    file_name: str = None
    thumbnail: str = None
    type: BaseFileType = None
