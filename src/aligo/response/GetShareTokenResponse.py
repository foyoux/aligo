"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class GetShareTokenResponse(DatClass, str):
    """..."""
    share_token: str = None
    expire_time: str = None
    expires_in: int = None
    share_id: str = None
    share_pwd: str = None

    def __new__(cls, *args, **kwargs):
        share_token = kwargs.get('share_token')
        if share_token is None:
            share_token = args[0]
        DatClass.__new__(cls, *args, **kwargs)
        return str.__new__(cls, share_token)

    def __str__(self):
        return self.share_token

    def __repr__(self):
        return f'{self.share_token!r}'
