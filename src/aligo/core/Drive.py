"""..."""
from typing import List

from aligo.core import BaseAligo
from aligo.core.Config import V2_DRIVE_GET, V2_DRIVE_GET_DEFAULT_DRIVE, V2_DRIVE_LIST_MY_DRIVES
from aligo.request import GetDriveRequest, GetDefaultDriveRequest
from aligo.response import ListMyDrivesResponse
from aligo.types import BaseDrive


class Drive(BaseAligo):
    """..."""

    def _core_get_drive(self, body: GetDriveRequest) -> BaseDrive:
        """..."""
        response = self.post(V2_DRIVE_GET, body=body)
        return self._result(response, BaseDrive)

    def get_default_drive(self) -> BaseDrive:
        """
        Get default drive.
        :return: [BaseDrive]

        :Example:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> drive = ali.get_default_drive()
        >>> print(drive.drive_name)
        """
        if self._default_drive is None:
            response = self.post(V2_DRIVE_GET_DEFAULT_DRIVE, body=GetDefaultDriveRequest(self._auth.token.user_id))
            self._default_drive = self._result(response, BaseDrive)
        return self._default_drive

    def list_my_drives(self) -> List[BaseDrive]:
        """
        List my drives.
        :return: [BaseDrive]

        :Example:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> drives = ali.list_my_drives()
        >>> for drive in drives:
        >>>     print(drive.drive_name)
        """
        # noinspection PyTypeChecker
        return list(self._list_file(V2_DRIVE_LIST_MY_DRIVES, {}, ListMyDrivesResponse))
