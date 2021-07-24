"""..."""
from dataclasses import dataclass
from typing import List

from aligo.types import DataClass, VideoTranscodeTemplate


@dataclass
class GetVideoPlayInfoResponse(DataClass):
    """..."""
    template_list: List[VideoTranscodeTemplate] = None

    # def __post_init__(self):
    #     self.template_list = _null_list(VideoTranscodeTemplate, self.template_list)
