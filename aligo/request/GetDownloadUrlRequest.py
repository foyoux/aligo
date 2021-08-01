"""获取下载链接请求"""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class GetDownloadUrlRequest(DataClass):
    """
    /**
   * 过期时间
   * 默认值 : 900
   * 最小值 : 0
   * 最大值 : 14400
   */
    """
    file_id: str = None
    file_name: str = None
    expire_sec: int = 14400
    drive_id: str = None
