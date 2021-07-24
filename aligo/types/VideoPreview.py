"""..."""
from dataclasses import dataclass
from typing import List

from .AudioMeta import AudioMeta
from .AudioMusicMeta import AudioMusicMeta
from .AudioTranscodeTemplate import AudioTranscodeTemplate
from .DataClass import DataClass
from .VideoPreviewSprite import VideoPreviewSprite
from .VideoTranscodeTemplate import VideoTranscodeTemplate


@dataclass
class VideoPreview(DataClass):
    """..."""
    video_format: str = None
    audio_format: str = None
    duration: str = None
    audio_sample_rate: str = None
    audio_channels: int = None
    audio_template_list: List[AudioTranscodeTemplate] = None
    audio_meta: AudioMeta = None
    audio_music_meta: AudioMusicMeta = None
    bitrate: str = None
    frame_rate: str = None
    height: int = None
    sprite_info: VideoPreviewSprite = None
    template_list: List[VideoTranscodeTemplate] = None
    thumbnail: str = None
    width: int = None

    # def __post_init__(self):
    #     self.audio_template_list = _null_list(AudioTranscodeTemplate, self.audio_template_list)
    #     self.audio_meta = _null_dict(AudioMeta, self.audio_meta)
    #     self.audio_music_meta = _null_dict(AudioMusicMeta, self.audio_music_meta)
    #     self.sprite_info = _null_dict(VideoPreviewSprite, self.sprite_info)
    #     self.template_list = _null_list(VideoTranscodeTemplate, self.template_list)
