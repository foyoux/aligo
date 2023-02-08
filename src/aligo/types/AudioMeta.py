"""..."""
# 导包基本原则
# 1. 包内相对导入: from .DataClass import DataClass
# 2. 包外包导入: from aligo.dataobj import xxx
from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class AudioMeta(DataClass):
    """..."""
    bitrate: int = None
    duration: int = None
    sample_rate: int = None
    channels: int = None
