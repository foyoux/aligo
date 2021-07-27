"""..."""
from dataclasses import dataclass
from typing import List

from aligo.types import DataClass, AudioTranscodeTemplate


@dataclass
class GetAudioPlayInfoResponse(DataClass):
    """..."""
    template_list: List[AudioTranscodeTemplate] = None
