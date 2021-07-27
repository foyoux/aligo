"""..."""
from dataclasses import dataclass

from aligo.types import *


@dataclass
class GetDownloadUrlResponse(DataClass):
    """..."""
    expiration: str
    method: str
    size: int
    url: str
    cdn_url: str
    internal_url: str
    ratelimit: RateLimit = None
