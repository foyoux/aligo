"""..."""
from dataclasses import dataclass
from typing import List

from aligo.types import DatClass, VideoTranscodeTemplate


@dataclass
class GetVideoPlayInfoResponse(DatClass):
    """..."""
    template_list: List[VideoTranscodeTemplate] = None
