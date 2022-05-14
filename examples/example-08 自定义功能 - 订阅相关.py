"""
1. 获取订阅页面推荐用户列表
2. 订阅用户
3. 取消订阅用户
4. 获取订阅用户列表
"""
from dataclasses import dataclass, field
from typing import List

from aligo import Aligo


@dataclass
class FollowUser:
    """订阅用户"""
    description: str = None
    avatar: str = None
    user_id: str = None
    nick_name: str = None
    phone: str = None
    is_following: bool = None
    has_unread_message: bool = None
    latest_messages: List[dict] = field(default_factory=list)


class CustomAligo(Aligo):
    """自定义Aligo类"""

    def user_recommend(self, limit: int = 20) -> List[FollowUser]:
        """获取订阅页面推荐用户列表"""
        resp = self._post('/adrive/v1/timeline/user/recommend', body={
            'limit': limit if limit <= 100 else 100,
            'order_by': "updated_at",
            'order_direction': "DESC",
            'user_id': self.user_id,  # 自己的user_id
        })
        items = resp.json()['items']
        return [FollowUser(**item) for item in items]

    def follow_user(self, user_id: str) -> bool:
        """订阅用户"""
        resp = self._post('/adrive/v1/member/follow_user', body={
            'user_id': user_id
        })
        return resp.status_code == 200

    def unfollow_user(self, user_id: str) -> bool:
        """取消订阅用户"""
        resp = self._post('/adrive/v1/member/unfollow_user', body={
            'user_id': user_id
        })
        return resp.status_code == 200

    def list_following(self, limit: int = 20) -> List[FollowUser]:
        """获取订阅用户列表"""
        resp = self._post('/adrive/v1/member/list_following', body={
            "limit": limit, "order_by": "updated_at", "order_direction": "DESC"
        })
        items = resp.json()['items']
        return [FollowUser(**item) for item in items]


if __name__ == '__main__':
    cali = CustomAligo()
    users = cali.list_following()
    for user in users:
        print(user)
