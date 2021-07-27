"""todo"""
from dataclasses import dataclass

from .Enum import BaseFileCategory, BaseFileType
from .DataClass import DataClass
from .ImageMedia import ImageMedia
from .VideoMedia import VideoMedia
from .VideoPreview import VideoPreview


@dataclass
class BaseShareFile(DataClass):
    """..."""
    share_id: str = None
    name: str = None
    size: int = None
    creator: str = None
    description: str = None
    category: BaseFileCategory = None
    download_url: str = None
    file_extension: str = None
    file_id: str = None
    thumbnail: str = None
    type: BaseFileType = None
    updated_at: str = None
    created_at: str = None
    url: str = None
    parent_file_id: str = None
    selected: bool = None
    image_media_metadata: ImageMedia = None
    video_media_metadata: VideoMedia = None
    video_preview_metadata: VideoPreview = None
