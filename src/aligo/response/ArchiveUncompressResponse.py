"""..."""

from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class ArchiveUncompressResponse(DataClass):
    """..."""
    state: str = None
    task_id: str = None
