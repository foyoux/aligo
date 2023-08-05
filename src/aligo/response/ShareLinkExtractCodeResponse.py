"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class ShareLinkExtractCodeResponse(DatClass):
    """..."""
    share_id: str = None
    share_pwd: str = None
