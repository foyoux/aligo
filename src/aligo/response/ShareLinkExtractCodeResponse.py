"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class ShareLinkExtractCodeResponse(DataClass):
    """..."""
    share_id: str = None
    share_pwd: str = None
