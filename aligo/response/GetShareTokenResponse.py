"""..."""
import base64
import json
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class GetShareTokenResponse(DataClass, str):
    """..."""
    share_token: str = None
    expire_time: str = None
    expires_in: int = None
    share_id: str = None

    def __new__(cls, *args, **kwargs):
        share_token = kwargs.get('share_token')
        if share_token is None:
            share_token = args[0]
        return super().__new__(cls, share_token)

    def __str__(self):
        return self.share_token

    def __repr__(self):
        return '\'' + self.share_token + '\''

    def __post_init__(self):
        custom_json = json.loads(base64.b64decode(self.share_token.split('.')[1] + '=='))['customJson']
        self.share_id = json.loads(custom_json)['share_id']
