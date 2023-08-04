"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class GetOfficePreviewUrlResponse(DatClass):
    """..."""
    access_token: str = None
    preview_url: str = None
