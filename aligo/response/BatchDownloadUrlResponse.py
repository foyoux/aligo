"""..."""
from dataclasses import dataclass

from aligo.types import DataClass
from .GetDownloadUrlResponse import GetDownloadUrlResponse


@dataclass
class BatchDownloadUrlResponse(DataClass):
    """..."""
    id: str = None
    status: int = None
    body: GetDownloadUrlResponse = None
    method: str = None
