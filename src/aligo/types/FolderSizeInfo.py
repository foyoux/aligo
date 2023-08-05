"""..."""
from dataclasses import dataclass

from .Type import DatClass


@dataclass
class FolderSizeInfo(DatClass):
    size: int = None
    file_count: int = None
    folder_count: int = None
