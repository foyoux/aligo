"""..."""
from dataclasses import dataclass

from aligo.types import DatClass
from aligo.types.Enum import BaseFileType, BaseFileCategory


@dataclass
class ShareItemInfo(DatClass):
    """..."""
    category: BaseFileCategory = None
    file_extension: str = None
    file_id: str = None
    file_name: str = None
    thumbnail: str = None
    type: BaseFileType = None
