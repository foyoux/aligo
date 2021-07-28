"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass


@dataclass
class BatchDownloadUrlRequest(DataClass):
    """..."""
    drive_id: str = None
    file_id_list: List[str] = field(default_factory=list)
    """
    /**
   * 过期时间
   * 默认值 : 900
   * 最小值 : 0
   * 最大值 : 14400
   */
    """
    expire_sec: int = 14400
