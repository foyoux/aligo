"""..."""
from dataclasses import dataclass

from aligo.types import DatClass
from aligo.types.Enum import ArchiveType


@dataclass
class ArchiveUncompressRequest(DatClass):
    """..."""
    file_id: str = None
    target_file_id: str = 'root'
    archive_type: ArchiveType = 'zip'
    drive_id: str = None
    target_drive_id: str = None
    domain_id: str = ''
