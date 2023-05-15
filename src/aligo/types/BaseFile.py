"""..."""
from dataclasses import dataclass, field
from typing import Dict, List

from .DataClass import DataClass
from .Enum import *
from .FieldsInfo import FieldsInfo
from .ImageMedia import ImageMedia
from .VideoMedia import VideoMedia
from .VideoPreview import VideoPreview


@dataclass
class BaseFile(DataClass):
    """..."""
    type: BaseFileType = None
    file_id: str = None
    name: str = None
    parent_file_id: str = field(default=None, repr=False)
    category: BaseFileCategory = field(default=None, repr=False)
    size: int = field(default=None, repr=False)
    created_at: str = field(default=None, repr=False)
    content_type: str = field(default=None, repr=False)
    description: str = field(default=None, repr=False)
    content_hash: str = field(default=None, repr=False)
    content_hash_name: BaseFileContentHashName = field(default=None, repr=False)
    crc64_hash: str = field(default=None, repr=False)
    domain_id: str = field(default=None, repr=False)
    download_url: str = field(default=None, repr=False)
    drive_id: str = field(default=None, repr=False)
    encrypt_mode: str = field(default=None, repr=False)
    file_extension: str = field(default=None, repr=False)
    hidden: bool = field(default=None, repr=False)
    image_media_metadata: ImageMedia = field(default=None, repr=False)
    labels: list = field(default=None, repr=False)
    meta: str = field(default=None, repr=False)
    mime_extension: str = field(default=None, repr=False)
    mime_type: str = field(default=None, repr=False)
    punish_flag: int = field(default=None, repr=False)
    starred: bool = field(default=None, repr=False)
    status: str = field(default=None, repr=False)
    streams_url_info: Dict = field(default=None, repr=False)
    streams_info: Dict = field(default=None, repr=False)
    thumbnail: str = field(default=None, repr=False)
    trashed: bool = field(default=None, repr=False)
    trashed_at: str = field(default=None, repr=False)
    updated_at: str = field(default=None, repr=False)
    upload_id: str = field(default=None, repr=False)
    url: str = field(default=None, repr=False)
    user_meta: str = field(default=None, repr=False)
    video_media_metadata: VideoMedia = field(default=None, repr=False)
    video_preview_metadata: VideoPreview = field(default=None, repr=False)
    location: str = field(default=None, repr=False)
    action_list: List[str] = field(default_factory=list, repr=False)
    user_tags: Dict = field(default=None, repr=False)
    last_modifier_type: str = field(default=None, repr=False)
    last_modifier_id: str = field(default=None, repr=False)
    last_modifier_name: str = field(default=None, repr=False)
    creator_type: str = field(default=None, repr=False)
    creator_id: str = field(default=None, repr=False)
    creator_name: str = field(default=None, repr=False)
    revision_id: str = field(default=None, repr=False)
    sync_flag: bool = field(default=None, repr=False)
    sync_device_flag: bool = field(default=None, repr=False)
    sync_meta: str = field(default=None, repr=False)
    ex_fields_info: FieldsInfo = field(default=None, repr=False)
    from_share_id: str = None
    revision_version: int = None
    channel: str = None
    meta_name_punish_flag: int = None
    meta_name_investigation_status: int = None
