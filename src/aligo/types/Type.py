from typing import TypeVar

from datclass import get_datclass

DataType = TypeVar('DataType')  # 泛型类型变量
DatClass = get_datclass(log=False)  # 使 dataclass 支持嵌套 和 扩展字段
