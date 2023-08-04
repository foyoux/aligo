"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class FolderSizeInfo(DatClass):
    size: int = None
    file_count: int = None
    folder_count: int = None
