"""Audio class"""

from aligo.core import *
from aligo.request import *
from aligo.response import *


class Audio(Core):
    """音频相关"""

    def get_audio_play_info(self, file_id: str, drive_id: str = None) -> GetAudioPlayInfoResponse:
        """
        官方：获取音频播放信息
        :param file_id: [str] 音频 file_id
        :param drive_id: Optional[str] 音频文件的 drive_id
        :return: [GetAudioPlayInfoResponse]

        用法示例：
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> audio = ali.get_audio_play_info('<file_id>')
        >>> print(audio)
        """
        body = GetAudioPlayInfoRequest(file_id=file_id, drive_id=drive_id)
        return self._core_get_audio_play_info(body)
