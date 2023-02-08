"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class GetShareTokenRequest(DataClass):
    """..."""
    share_id: str
    share_pwd: str = ''
