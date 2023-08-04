"""..."""
from dataclasses import dataclass

from datclass import DatClass


@dataclass
class FieldsInfo(DatClass):
    """..."""
    image_count: int = 0
    video_meta_processed: str = None
    story_ids: str = None
