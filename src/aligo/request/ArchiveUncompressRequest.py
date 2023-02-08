"""..."""
from dataclasses import dataclass

from aligo.types import DataClass
from aligo.types.Enum import ArchiveType

@dataclass
class ArchiveUncompressRequest(DataClass):
    """..."""
    file_id: str = None
    target_file_id: str = 'root'
    archive_type: ArchiveType = 'zip'
    drive_id: str = None
    target_drive_id: str = None
    domain_id: str = ''
