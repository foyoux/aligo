"""..."""
from dataclasses import dataclass

from aligo.types import DatClass, VideoPreviewPlayInfo


@dataclass
class GetVideoPreviewPlayInfoResponse(DatClass):
    """..."""
    domain_id: str = None
    drive_id: str = None
    file_id: str = None
    category: str = None
    video_preview_play_info: VideoPreviewPlayInfo = None
