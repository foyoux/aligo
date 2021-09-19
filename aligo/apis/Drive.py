"""drive"""

from aligo.core import *
from aligo.request import *
from aligo.types import *


class Drive(Core):
    """..."""

    def get_drive(self, drive_id: str = None) -> BaseDrive:
        """获取 drive"""
        body = GetDriveRequest(drive_id=drive_id)
        return self._core_get_drive(body)
