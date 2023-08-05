"""..."""
from aligo.core import BaseAligo
from aligo.core.Config import V2_DATABOX_GET_AUDIO_PLAY_INFO
from aligo.request import GetAudioPlayInfoRequest
from aligo.response import GetAudioPlayInfoResponse


class Audio(BaseAligo):
    """..."""

    def _core_get_audio_play_info(self, body: GetAudioPlayInfoRequest) -> GetAudioPlayInfoResponse:
        """获取音频播放信息"""
        response = self.post(V2_DATABOX_GET_AUDIO_PLAY_INFO, body=body)
        return self._result(response, GetAudioPlayInfoResponse)
