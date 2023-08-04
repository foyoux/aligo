"""..."""
from dataclasses import dataclass

from datclass import DatClass

from .Enum import MediaTranscodeStatus


@dataclass
class VideoTranscodeTemplate(DatClass):
    """..."""
    template_id: str = None
    status: MediaTranscodeStatus = None
    url: str = None
