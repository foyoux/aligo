"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class ArchiveUncompressResponse(DatClass):
    """..."""
    state: str = None
    task_id: str = None
