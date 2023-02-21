"""..."""
from typing import List, Union

from aligo.core import *
from aligo.core.Config import *
from aligo.request import AlbumListRequest, AlbumListFilesRequest
from aligo.types import ListAlbumItem, BaseAlbum, BaseFile
from aligo.types.Enum import *


class Album(Core):
    """..."""

    def list_albums(
            self, album_drive_id: str = None,
            order_by: GetShareLinkListOrderBy = 'created_at',
            order_direction: OrderDirection = 'DESC', drive_id=None
    ) -> List[ListAlbumItem]:
        """获取相册列表"""
        album_drive_id = album_drive_id or self.album_info.driveId
        drive_id = drive_id or self.default_drive_id
        body = AlbumListRequest(
            album_drive_id=album_drive_id, drive_id=drive_id,
            order_by=order_by, order_direction=order_direction
        )
        return list(self._core_list_album(body))

    def delete_album(self, album_id: str) -> bool:
        """删除 album"""
        response = self._post(ADRIVE_V1_ALBUM_DELETE, body={'album_id': album_id})
        return response.status_code == 200

    def create_album(self, name: str, description: str = None) -> BaseAlbum:
        """创建 album"""
        response = self._post(ADRIVE_V1_ALBUM_CREATE, body={
            'name': name,
            'description': description
        })
        return self._result(response, BaseAlbum)

    def get_album(self, album_id: str) -> BaseAlbum:
        """获取相册，通过 album_id"""
        response = self._post(ADRIVE_V1_ALBUM_GET, body={'album_id': album_id})
        return self._result(response, BaseAlbum)

    def add_files_to_album(self, album_id: str, files: List[Union[BaseFile, str]]) -> List[BaseFile]:
        response = self._post(ADRIVE_V1_ALBUM_ADD_FILES, body={
            'album_id': album_id,
            'drive_file_list': [{'drive_id': f.drive_id, 'file_id': f.file_id} for f in files]
        })
        return self._result(response, BaseFile, field='file_list')

    def list_album_files(self, album_id: str, order_direction: OrderDirection = 'DESC') -> List[BaseFile]:
        """获取指定相册文件"""
        body = AlbumListFilesRequest(album_id=album_id, order_direction=order_direction)
        result = self._core_list_album_files(body)
        return list(result)

    def rename_album(self, album_id: str, name: str):
        response = self._post(ADRIVE_V1_ALBUM_UPDATE, body={
            'album_id': album_id,
            'name': name
        })
        return self._result(response, BaseAlbum)
