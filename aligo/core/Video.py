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
