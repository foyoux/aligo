"""..."""

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *


class Video(BaseAligo):
    """..."""

    def get_video_play_info(self, body: GetVideoPlayInfoRequest) -> GetVideoPlayInfoResponse:
        """..."""
        response = self._post(V2_DATABOX_GET_VIDEO_PLAY_INFO, body=body)
        return self._result(response, GetVideoPlayInfoResponse)

    # @lru_memoize()
    # def _cache_get_video_play_info(self, drive_id, file_id) -> GetVideoPlayInfoResponse:
    #     body = GetVideoPlayInfoRequest(drive_id=drive_id, file_id=file_id)
    #     response = self._post(V2_DATABOX_GET_VIDEO_PLAY_INFO, body=body)
    #     return self._result(response, GetVideoPlayInfoResponse)
    #
    # @overload
    # def get_video_play_info(self, body: GetVideoPlayInfoRequest, f5: bool = False) -> GetVideoPlayInfoResponse:
    #     """..."""
    #     ...
    #
    # @overload
    # def get_video_play_info(self, body: BaseFile, f5: bool = False) -> GetVideoPlayInfoResponse:
    #     """..."""
    #     ...
    #
    # @overload
    # def get_video_play_info(self, file_id: str,
    #                         drive_id: str = None, f5: bool = False) -> GetVideoPlayInfoResponse:
    #     """..."""
    #     ...
    #
    # def get_video_play_info(
    #         self,
    #         body: Union[GetVideoPlayInfoRequest, BaseFile] = None,
    #         file_id: str = None,
    #         drive_id: str = None,
    #         f5: bool = False
    # ) -> GetVideoPlayInfoResponse:
    #     """..."""
    #     if body is None:
    #         body = GetVideoPlayInfoRequest(drive_id=drive_id, file_id=file_id)
    #     if body.drive_id is None:
    #         body.drive_id = self.default_drive_id
    #     params = {'drive_id': body.drive_id, 'file_id': body.file_id}
    #     if f5:
    #         key = self._cache_get_video_play_info.cache_key(self=self, **params)
    #         self._cache_get_video_play_info.cache.delete(key)
    #     return self._cache_get_video_play_info(**params)
