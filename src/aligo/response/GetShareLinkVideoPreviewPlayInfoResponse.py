from dataclasses import dataclass, field
from typing import List

from aligo.types import DatClass


@dataclass
class LiveTranscodingTaskList(DatClass):
    keep_original_resolution: bool = None
    preview_url: str = None
    stage: str = None
    status: str = None
    template_height: int = None
    template_id: str = None
    template_name: str = None
    template_width: int = None
    url: str = None


@dataclass
class Meta(DatClass):
    duration: float = None
    height: int = None
    width: int = None


@dataclass
class VideoPreviewPlayInfo(DatClass):
    category: str = None
    live_transcoding_task_list: List[LiveTranscodingTaskList] = field(default_factory=list)
    meta: Meta = None


@dataclass
class GetShareLinkVideoPreviewPlayInfoResponse(DatClass):
    category: str = None
    file_id: str = None
    share_id: str = None
    video_preview_play_info: VideoPreviewPlayInfo = None
