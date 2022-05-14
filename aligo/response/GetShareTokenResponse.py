"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class GetShareTokenResponse(DataClass, str):
    """..."""

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, kwargs['share_token'])

    share_token: str = None
    expire_time: str = None
    expires_in: int = None
