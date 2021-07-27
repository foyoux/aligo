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
