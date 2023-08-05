"""..."""
from dataclasses import dataclass
from typing import List

from aligo.types import DatClass, AudioTranscodeTemplate


@dataclass
class GetAudioPlayInfoResponse(DatClass):
    """..."""
    template_list: List[AudioTranscodeTemplate] = None
