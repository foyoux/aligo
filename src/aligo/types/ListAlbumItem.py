"""..."""
from dataclasses import dataclass
from dataclasses import field
from typing import List, Dict

from .Type import DatClass


@dataclass
class ImageTags(DatClass):
    confidence: float = None
    name: str = None
    parent_name: str = None
    tag_level: int = None


@dataclass
class ImageQuality(DatClass):
    overall_score: float = None


@dataclass
class ImageMediaMetadata(DatClass):
    exif: str = None
    height: int = None
    image_quality: ImageQuality = None
    image_tags: List[ImageTags] = field(default_factory=list)
    width: int = None


@dataclass
class CoverItem(DatClass):
    category: str = None
    content_hash: str = None
    content_hash_name: str = None
    content_type: str = None
    crc64_hash: str = None
    created_at: str = None
    domain_id: str = None
    download_url: str = None
    drive_id: str = None
    encrypt_mode: str = None
    ex_fields_info: Dict = None
    file_extension: str = None
    file_id: str = None
    hidden: bool = None
    image_media_metadata: ImageMediaMetadata = None
    labels: List[str] = field(default_factory=list)
    mime_type: str = None
    name: str = None
    parent_file_id: str = None
    punish_flag: int = None
    size: int = None
    starred: bool = None
    status: str = None
    sync_flag: bool = None
    thumbnail: str = None
    trashed: bool = None
    type: str = None
    updated_at: str = None
    upload_id: str = None
    url: str = None
    user_meta: str = None


@dataclass
class Cover(DatClass):
    list: List[CoverItem] = field(default_factory=list)


@dataclass
class ListAlbumItem(DatClass):
    """..."""
    album_id: str = None
    cover: Cover = None
    created_at: int = None
    description: str = None
    file_count: int = None
    image_count: int = None
    name: str = None
    owner: str = None
    updated_at: int = None
    video_count: int = None
