"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class RestoreFileResponse(DataClass):
    """..."""
    async_task_id: str = None
    domain_id: str = None
    drive_id: str = None
    file_id: str = None
