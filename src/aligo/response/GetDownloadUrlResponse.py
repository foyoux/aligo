"""..."""
from dataclasses import dataclass

from aligo.types import DatClass, RateLimit
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
    domain_id: str = None
    drive_id: str = None
    encrypt_url: str = None
    file_id: str = None
    meta_name_investigation_status: int = None
    meta_name_punish_flag: int = None
    punish_flag: int = None
    revision_id: str = None
