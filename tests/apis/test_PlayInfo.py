"""测试get_audio_info方法"""
from aligo import *

PlayInfo_folder = '60f894f462ef3d9c57b344558454fbfb666de986'
audio_file_id = '60f89517c7e0bd37b8234d57af805cd76895ce84'
video_file_id = '60f89518ffd8497344f048c89fe465c103904337'


def test_play_info():
    """..."""
    ali = Aligo()

    audio_info = ali.get_audio_play_info(file_id=audio_file_id)
    assert isinstance(audio_info, GetAudioPlayInfoResponse)
    assert len(audio_info.template_list) > 0

    video_info = ali.get_video_preview_play_info(file_id=video_file_id)
    assert isinstance(video_info, GetVideoPreviewPlayInfoResponse)
    assert len(video_info.video_preview_play_info.live_transcoding_task_list) > 0
