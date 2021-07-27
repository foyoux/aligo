"""..."""
from dataclasses import dataclass, field

from aligo.types import *


@dataclass
class CopyFileResponse(DataClass):
    """..."""
    file_id: str = None
    drive_id: str = None
    domain_id: str = field(default=None, repr=False)
    async_task_id: str = field(default=None, repr=False)
