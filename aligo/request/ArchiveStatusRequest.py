"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class ArchiveStatusRequest(DataClass):
    """..."""
    file_id: str = None
    task_id: str = None
    drive_id: str = None
    domain_id: str = None
