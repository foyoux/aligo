"""..."""
from dataclasses import dataclass

from aligo.types import DatClass


@dataclass
class CancelShareLinkResponse(DatClass):
    """..."""
    # 这只是一个占位属性
    # 取消分享, 服务器返回为 '', 此对象仅用作与 Null对象 区分和统一结构和用法
    result: str = ''
