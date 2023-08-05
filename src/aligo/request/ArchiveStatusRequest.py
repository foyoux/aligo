"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class ArchiveStatusRequest(DatClass):
    """..."""
    file_id: str = None
    task_id: str = None
    drive_id: str = None
    domain_id: str = None
