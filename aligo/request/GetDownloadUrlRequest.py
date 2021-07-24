"""todo"""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class GetDownloadUrlRequest(DataClass):
    """..."""
    drive_id: str = None
    """
    /**
   * 过期时间
   * 默认值 : 900
   * 最小值 : 0
   * 最大值 : 14400
   */
    """
    expire_sec: int = None
    file_id: str = None
    file_name: str = None
