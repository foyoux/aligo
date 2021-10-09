"""..."""
from dataclasses import dataclass, field
from typing import List

from .FaceThumbnail import FaceThumbnail
from .CroppingSuggestionItem import CroppingSuggestionItem
from .DataClass import DataClass
from .ImageQuality import ImageQuality
from .SystemTag import SystemTag


@dataclass
class ImageMedia(DataClass):
    """..."""
    time: str = None
    faces: str = None
    city: str = None
    country: str = None
    address_line: str = None
    exif: str = None
    cropping_suggestion: List[CroppingSuggestionItem] = field(default_factory=list)
    district: str = None
    height: int = None
    image_quality: ImageQuality = None
    image_tags: List[SystemTag] = None
    location: str = None
    province: str = None
    story_image_score: int = None
    township: str = None
    width: int = None
    faces_thumbnail: List[FaceThumbnail] = field(default_factory=list)
