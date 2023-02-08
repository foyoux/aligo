"""..."""
from dataclasses import dataclass
from typing import List

from aligo.types import DataClass, VideoTranscodeTemplate


@dataclass
class GetVideoPlayInfoResponse(DataClass):
    """..."""
    template_list: List[VideoTranscodeTemplate] = None
