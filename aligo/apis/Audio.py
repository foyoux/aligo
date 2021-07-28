"""..."""

from aligo.core import *
from aligo.request import *
from aligo.response import *


class Audio(Core):
    """..."""

    def get_audio_play_info(self, file_id: str, drive_id: str = None) -> GetAudioPlayInfoResponse:
        """获取音频播放信息"""
        body = GetAudioPlayInfoRequest(file_id=file_id, drive_id=drive_id)
        return super(Audio, self).get_audio_play_info(body)
