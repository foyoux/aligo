"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class GetShareTokenRequest(DatClass):
    """..."""
    share_id: str
    share_pwd: str = ''
