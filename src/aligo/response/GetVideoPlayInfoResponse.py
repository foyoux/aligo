"""..."""
from dataclasses import dataclass
from typing import List

from datclass import DatClass

from aligo.types import VideoTranscodeTemplate


@dataclass
class GetVideoPlayInfoResponse(DatClass):
    """..."""
    template_list: List[VideoTranscodeTemplate] = None
