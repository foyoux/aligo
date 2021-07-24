"""..."""
from dataclasses import dataclass

from .BaseFile import BaseFile


@dataclass
class ShareLinkBaseFile(BaseFile):
    """..."""
    mime_type: str = None
    mime_extension: str = None
