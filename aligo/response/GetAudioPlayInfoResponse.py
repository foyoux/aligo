"""..."""
from dataclasses import dataclass
from typing import List

from aligo.types import DataClass, AudioTranscodeTemplate


@dataclass
class GetAudioPlayInfoResponse(DataClass):
    """..."""
    template_list: List[AudioTranscodeTemplate] = None

    # def __post_init__(self):
    #     self.template_list = _null_list(AudioTranscodeTemplate, self.template_list)
