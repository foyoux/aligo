"""..."""
from dataclasses import dataclass

from datclass import DatClass

from aligo.types import *
from aligo.types.Enum import BaseFileContentHashName


@dataclass
class GetDownloadUrlResponse(DatClass):
    """..."""
    expiration: str = None
    method: str = None
    size: int = None
    url: str = None
    cdn_url: str = None
    internal_url: str = None
    ratelimit: RateLimit = None
    crc64_hash: str = None
    content_hash: str = None
    content_hash_name: BaseFileContentHashName = None
