from typing import Iterator

from aligo.core import *
from aligo.core.Config import *
from aligo.request import AlbumListRequest
from aligo.response import AlbumInfoResponse, AlbumListResponse
from aligo.types import DataClass, BaseAlbum


class Album(BaseAligo):

    def get_albums_info(self) -> AlbumInfoResponse:
        response = self._post(ADRIVE_V1_USER_ALBUMS_INFO)
        data = response.json()['data']
        return DataClass.fill_attrs(AlbumInfoResponse, data)

    def _core_list_album(self, body: AlbumListRequest) -> Iterator[BaseAlbum]:
        yield from self._list_file(ADRIVE_V1_ALBUMHOME_ALBUMLIST, body, AlbumListResponse)
