"""..."""

from dataclasses import dataclass

from .DataClass import DataClass
from .Enum import MediaTranscodeStatus


@dataclass
class MediaTransCodeTemplate(DataClass):
    """..."""
    template_id: str = None
    status: MediaTranscodeStatus = None
    url: str = None
