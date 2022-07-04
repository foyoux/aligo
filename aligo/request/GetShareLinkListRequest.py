"""..."""
from dataclasses import dataclass

from aligo.types import *
from aligo.types.Enum import *


@dataclass
class GetShareLinkListRequest(DataClass):
    """获取自己的分享列表

    Attributes:
        creator (str): 一 、管理员：1.1 不传，查所有用户 1.2 传指定user_id，查指定用户的分享。
            * 二、普通用户：2.1 不传，查自己2.2 传指定user_id，只能是自己，否则报403
        limit (int): 返回数据最大条数,范围:[1-100]，默认:100
        marker (str):
        order_by (GetShareLinkListOrderBy): 排序字段,默认按照创建时间倒序输出。
        order_direction (str):
        include_canceled (bool): 列举结果是否包含已经取消的分享
    """
    creator: str = None
    limit: int = 100
    marker: str = ''
    order_by: GetShareLinkListOrderBy = 'created_at'
    order_direction: OrderDirection = 'DESC'
    include_canceled: bool = False
