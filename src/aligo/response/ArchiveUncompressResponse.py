"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class ArchiveUncompressResponse(DatClass):
    """..."""
    state: str = None
    task_id: str = None
