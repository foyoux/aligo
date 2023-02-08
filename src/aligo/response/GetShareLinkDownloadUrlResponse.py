"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import *


@dataclass
class GetShareLinkDownloadUrlResponse(DataClass):
    """..."""
    download_url: str = None
    url: str = None
    thumbnail: str = None
    video_template_list: List[VideoTranscodeTemplate] = field(default_factory=list)
    audio_template_list: List[AudioTranscodeTemplate] = field(default_factory=list)
