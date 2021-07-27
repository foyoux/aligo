"""..."""
from dataclasses import dataclass

from .MediaTransCodeTemplate import MediaTransCodeTemplate
from .Enum import MediaTranscodeStatus


@dataclass
class AudioTranscodeTemplate(MediaTransCodeTemplate):
    """..."""
    template_id: str = None
    status: MediaTranscodeStatus = None
    url: str = None
