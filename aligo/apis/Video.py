"""..."""

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types.Enum import VideoTemplateID


class Video(Core):
    """..."""

    def get_video_play_info(self, file_id: str, drive_id: str = None) -> GetVideoPlayInfoResponse:
        """获取视频播放信息"""
        body = GetVideoPlayInfoRequest(file_id=file_id, drive_id=drive_id)
        return self._core_get_video_play_info(body)

    def get_video_preview_play_info(self, file_id: str, template_id: VideoTemplateID = '',
                                    drive_id: str = None) -> GetVideoPreviewPlayInfoResponse:
        """获取视频播放信息"""
        body = GetVideoPreviewPlayInfoRequest(file_id=file_id, template_id=template_id, drive_id=drive_id)
        return self._core_get_video_preview_play_info(body)
