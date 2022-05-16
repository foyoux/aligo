"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class GetShareTokenResponse(DataClass, str):
    """..."""

    def __new__(cls, *args, **kwargs):
        share_token = kwargs.get('share_token')
        if share_token is None:
            share_token = args[0]
        return super().__new__(cls, share_token)

    share_token: str = None
    expire_time: str = None
    expires_in: int = None

    def __str__(self):
        return self.share_token
