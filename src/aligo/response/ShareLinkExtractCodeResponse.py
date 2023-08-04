"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class ShareLinkExtractCodeResponse(DatClass):
    """..."""
    share_id: str = None
    share_pwd: str = None
