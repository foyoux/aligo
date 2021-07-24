"""..."""

from dataclasses import dataclass

from aligo.config import MediaTranscodeStatus
from .MediaTransCodeTemplate import MediaTransCodeTemplate


@dataclass
class VideoTranscodeTemplate(MediaTransCodeTemplate):
    """..."""
    template_id: str = None
    status: MediaTranscodeStatus = None
    url: str = None
