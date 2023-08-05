"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class GetShareTokenRequest(DatClass):
    """..."""
    share_id: str
    share_pwd: str = ''
