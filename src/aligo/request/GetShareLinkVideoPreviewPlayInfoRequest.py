"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class GetShareLinkVideoPreviewPlayInfoRequest(DatClass):
    """..."""
    file_id: str
    drive_id: str
    share_id: str
    category: str = 'live_transcoding'
    get_preview_url: bool = True
    get_subtitle_info: bool = True
    mode: str = 'high_res'
    template_id: str = ''
    url_expire_sec: int = 600
