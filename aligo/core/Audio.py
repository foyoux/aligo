"""..."""

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *


class Audio(BaseAligo):
    """..."""

    def get_audio_play_info(self, body: GetAudioPlayInfoRequest) -> GetAudioPlayInfoResponse:
        """获取音频播放信息"""
        response = self._post(V2_DATABOX_GET_AUDIO_PLAY_INFO, body=body)
        return self._result(response, GetAudioPlayInfoResponse)

    # @lru_memoize()
    # def _cache_get_audio_play_info(self, drive_id, file_id) -> GetAudioPlayInfoResponse:
    #     body = GetAudioPlayInfoRequest(drive_id=drive_id, file_id=file_id)
    #     response = self._post(V2_DATABOX_GET_AUDIO_PLAY_INFO, body=body)
    #     return self._result(response, GetAudioPlayInfoResponse)
    #
    # @overload
    # def get_audio_play_info(self, body: GetAudioPlayInfoRequest, f5: bool = False) -> GetAudioPlayInfoResponse:
    #     """..."""
    #     ...
    #
    # @overload
    # def get_audio_play_info(self, body: BaseFile, f5: bool = False) -> GetAudioPlayInfoResponse:
    #     """..."""
    #     ...
    #
    # @overload
    # def get_audio_play_info(self, file_id: str,
    #                         drive_id: str = None, f5: bool = False) -> GetAudioPlayInfoResponse:
    #     """..."""
    #     ...
    #
    # def get_audio_play_info(self, body: Union[GetAudioPlayInfoRequest, BaseFile] = None, file_id: str = None,
    #                         drive_id: str = None,
    #                         f5: bool = False) -> GetAudioPlayInfoResponse:
    #     """..."""
    #     if body is None:
    #         body = GetAudioPlayInfoRequest(file_id=file_id, drive_id=drive_id)
    #     if body.drive_id is None:
    #         body.drive_id = self.default_drive_id
    #     params = {'drive_id': body.drive_id, 'file_id': body.file_id}
    #     if f5:
    #         key = self._cache_get_audio_play_info.cache_key(self=self, **params)
    #         self._cache_get_audio_play_info.cache.delete(key)
    #     return self._cache_get_audio_play_info(**params)
