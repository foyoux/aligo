"""..."""
from dataclasses import dataclass
from typing import List

from datclass import DatClass

from aligo.types import AudioTranscodeTemplate


@dataclass
class GetAudioPlayInfoResponse(DatClass):
    """..."""
    template_list: List[AudioTranscodeTemplate] = None
