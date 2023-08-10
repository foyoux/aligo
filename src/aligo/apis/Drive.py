"""drive"""
from aligo.core import Core
from aligo.core.Config import ADRIVE_V1_USER_DRIVE_CAPACITY_DETAILS
from aligo.request import GetDriveRequest
from aligo.types import BaseDrive, DriveCapacityDetail


class Drive(Core):
    """..."""

    def get_drive(self, drive_id: str = None) -> BaseDrive:
        """
        获取 drive 信息
        :param drive_id: Optional[str] drive id，默认：None，如果为 None，则返回当前登录用户的 drive 信息
        :return: [BaseDrive]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.get_drive()
        >>> print(result)
        """
        body = GetDriveRequest(drive_id=drive_id)
        return self._core_get_drive(body)

    def drive_capacity_details(self) -> DriveCapacityDetail:
        """获取网盘容量详细信息"""
        response = self.post(ADRIVE_V1_USER_DRIVE_CAPACITY_DETAILS)
        return self._result(response, DriveCapacityDetail)
