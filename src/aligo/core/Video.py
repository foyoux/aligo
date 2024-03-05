"""..."""
from aligo.core import BaseAligo
from aligo.core.Config import V2_DATABOX_GET_VIDEO_PLAY_INFO, V2_FILE_GET_VIDEO_PREVIEW_PLAY_INFO
from aligo.request import GetVideoPlayInfoRequest, GetVideoPreviewPlayInfoRequest
from aligo.response import *


class Video(BaseAligo):
    """..."""

    def _core_get_video_play_info(self, body: GetVideoPlayInfoRequest) -> GetVideoPlayInfoResponse:
        """..."""
        raise NotImplementedError('视频预览功能已下线')
        response = self.post(V2_DATABOX_GET_VIDEO_PLAY_INFO, body=body)
        return self._result(response, GetVideoPlayInfoResponse)

    def _core_get_video_preview_play_info(
            self,
            body: GetVideoPreviewPlayInfoRequest
    ) -> GetVideoPreviewPlayInfoResponse:
        """可获取m3u8链接"""
        response = self.post(V2_FILE_GET_VIDEO_PREVIEW_PLAY_INFO, body=body)
        return self._result(response, GetVideoPreviewPlayInfoResponse)
