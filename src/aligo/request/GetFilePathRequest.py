"""GetFilePathRequest"""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class GetFilePathRequest(DatClass):
    """GetFilePathRequest"""
    file_id: str = None
    drive_id: str = None
