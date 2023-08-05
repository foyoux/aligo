"""..."""
from dataclasses import dataclass, field
from typing import List

from .Enum import VideoTemplateID
from .Type import DatClass


@dataclass
class LiveTranscodingMeta(DatClass):
    """..."""
    ts_segment: int = None
    ts_total_count: int = None
    ts_pre_count: int = None


@dataclass
class Meta(DatClass):
    """..."""
    duration: float = None
    width: int = None
    height: int = None
    live_transcoding_meta: LiveTranscodingMeta = None


@dataclass
class LiveTranscodingTask(DatClass):
    """..."""
    template_id: VideoTemplateID = None
    status: str = None
    stage: str = None
    url: str = None
    template_name: str = None
    template_width: int = None
    template_height: int = None


@dataclass
class VideoPreviewPlayInfo(DatClass):
    """..."""
    category: str = None
    meta: Meta = None
    live_transcoding_task_list: List[LiveTranscodingTask] = field(default_factory=list)
