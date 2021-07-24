"""..."""

from dataclasses import dataclass

from .DataClass import DataClass
from aligo.config import MediaTranscodeStatus


@dataclass
class MediaTransCodeTemplate(DataClass):
    """..."""
    template_id: str = None
    status: MediaTranscodeStatus = None
    url: str = None
