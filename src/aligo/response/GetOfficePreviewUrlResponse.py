"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class GetOfficePreviewUrlResponse(DataClass):
    """..."""
    access_token: str = None
    preview_url: str = None
