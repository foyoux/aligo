"""基本分享文件"""
from dataclasses import dataclass, field
from typing import List

from .DataClass import DataClass
from .Enum import BaseFileCategory, BaseFileType
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
    # 2021年07月29日16时15分41秒
    mime_extension: str = None
    mime_type: str = None
    punish_flag: int = 0
    # 2021年08月31日17时56分14秒
    action_list: List[str] = field(default_factory=list, repr=False)
    # 2022年01月27日11时17分54秒
    drive_id: str = None
    domain_id: str = None
    revision_id: str = None
    # 2022年11月21日13时25分58秒
    starred: bool = False
    content_hash: str = None
    trashed_at: str = None
    from_share_id : str = None
