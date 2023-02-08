"""..."""

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types.Enum import VideoTemplateID


class Video(Core):
    """..."""

    def get_video_play_info(self, file_id: str, drive_id: str = None) -> GetVideoPlayInfoResponse:
        """
        获取视频播放信息
        :param file_id: [必须] 视频文件ID
        :param drive_id: [可选] 文件所在的网盘盘符ID
        :return: [GetVideoPlayInfoResponse]

        :Example:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> video = ali.get_video_play_info('<file_id>')
        >>> print(video)
        """
        body = GetVideoPlayInfoRequest(file_id=file_id, drive_id=drive_id)
        return self._core_get_video_play_info(body)

    def get_video_preview_play_info(self, file_id: str, template_id: VideoTemplateID = '',
                                    drive_id: str = None) -> GetVideoPreviewPlayInfoResponse:
        """
        获取视频预览播放信息
        :param file_id: [必须] 视频文件ID
        :param template_id: [可选] 视频模板ID
        :param drive_id: [可选] 文件所在的网盘盘符ID
        :return: [GetVideoPreviewPlayInfoResponse]

        :Example:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> video = ali.get_video_preview_play_info('<file_id>')
        >>> print(video)
        """
        body = GetVideoPreviewPlayInfoRequest(file_id=file_id, template_id=template_id, drive_id=drive_id)
        return self._core_get_video_preview_play_info(body)
