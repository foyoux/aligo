"""..."""

from aligo.core import *
from aligo.core.Config import *
from aligo.types import *


class User(BaseAligo):
    """..."""

    def get_user(self, f5: bool = False) -> BaseUser:
        """..."""
        if self._user is None or f5:
            response = self._post(V2_USER_GET)
            # response.status_code == 200 or self._error_log_exit(response)
            # self._user = BaseUser(**response.json())
            self._user = self._result(response, BaseUser)
        return self._user
