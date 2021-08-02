"""..."""

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.types import *


class Drive(BaseAligo):
    """..."""

    def get_drive(self, body: GetDriveRequest) -> BaseDrive:
        """..."""
        response = self._post(V2_DRIVE_GET, body=body)
        return self._result(response, BaseDrive)

    def get_default_drive(self) -> BaseDrive:
        """..."""
        if self._default_drive is None:
            response = self._post(V2_DRIVE_GET_DEFAULT_DRIVE, body=GetDefaultDriveRequest(self._token.user_id))
            self._default_drive = self._result(response, BaseDrive)
        return self._default_drive
