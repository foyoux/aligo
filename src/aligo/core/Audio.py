"""..."""

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *


class Audio(BaseAligo):
    """..."""

    def _core_get_audio_play_info(self, body: GetAudioPlayInfoRequest) -> GetAudioPlayInfoResponse:
        """获取音频播放信息"""
        response = self._post(V2_DATABOX_GET_AUDIO_PLAY_INFO, body=body)
        return self._result(response, GetAudioPlayInfoResponse)
