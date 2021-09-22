"""GetFilePathRequest"""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class GetFilePathRequest(DataClass):
    """GetFilePathRequest"""
    file_id: str = None
    drive_id: str = None
