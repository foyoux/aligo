"""..."""
from dataclasses import dataclass

from aligo.types import DataClass
from aligo.types.Enum import GetVideoPreviewCategory, VideoTemplateID


@dataclass
class GetVideoPreviewPlayInfoRequest(DataClass):
    """..."""
    file_id: str = None
    drive_id: str = None
    category: GetVideoPreviewCategory = 'live_transcoding'
    template_id: VideoTemplateID = None
    url_expire_sec: int = 14400
