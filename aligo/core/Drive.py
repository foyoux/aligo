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

    # @lru_memoize()  # all params must be hashable, dataclass must set unsafe_hash=True
    # def _cache_get_drive(self, drive_id: str) -> BaseDrive:
    #     body = GetDriveRequest(drive_id=drive_id)
    #     response = self._post(V2_DRIVE_GET, body=body)
    #     return self._result(response, BaseDrive)
    #
    # def get_drive(self, drive_id: str = None, f5: bool = False) -> BaseDrive:
    #     """
    #     If not provider body, this func is equals get_default_drive
    #     """
    #     if drive_id is None:
    #         drive_id = self.default_drive_id
    #     params = {'drive_id': drive_id}
    #
    #     if f5:
    #         key = self._cache_get_drive.cache_key(self=self, **params)
    #         self._cache_get_drive.cache.delete(key)
    #     return self._cache_get_drive(**params)
