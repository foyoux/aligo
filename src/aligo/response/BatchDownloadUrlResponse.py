"""..."""
from dataclasses import dataclass

from datclass import DatClass

from .GetDownloadUrlResponse import GetDownloadUrlResponse


@dataclass
class BatchDownloadUrlResponse(DatClass):
    """..."""
    id: str = None
    status: int = None
    body: GetDownloadUrlResponse = None
    method: str = None
