"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class GetOfficePreviewUrlResponse(DatClass):
    """..."""
    access_token: str = None
    preview_url: str = None
