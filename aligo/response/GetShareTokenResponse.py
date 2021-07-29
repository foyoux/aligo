"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class GetShareTokenResponse(DataClass):
    """..."""
    share_token: str = None
    expire_time: str = None
    expires_in: int = None
