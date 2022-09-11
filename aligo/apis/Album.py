"""..."""
from aligo.core import *
from aligo.request import AlbumListRequest
from aligo.types.Enum import *


class Album(Core):
    """..."""

    def list_albums(
            self, album_drive_id: str,
            order_by: GetShareLinkListOrderBy = 'created_at',
            order_direction: OrderDirection = 'DESC', drive_id=None
    ):
        """获取相册列表"""
        drive_id = drive_id or self.default_drive_id
        body = AlbumListRequest(
            album_drive_id=album_drive_id, drive_id=drive_id,
            order_by=order_by, order_direction=order_direction
        )
        return list(self._core_list_album(body))
