"""..."""
from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class FieldsInfo(DataClass):
    """..."""
    image_count: int = 0
    video_meta_processed: str = None
    story_ids: str = None
