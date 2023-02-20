"""..."""
from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class FolderSizeInfo(DataClass):
    size: int = None
    file_count: int = None
    folder_count: int = None
