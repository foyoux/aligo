"""..."""
from dataclasses import dataclass, field

from .DataClass import DataClass


@dataclass
class UserConfig(DataClass):
    """
    {
      "id": 601978,
      "face_ai_recognition_status": 1,
      "auto_generate_memory": 0,
      "is_sfiia_entry_hidden": false,
      "homepage_visibility": 1,
      "folder_cover_enable": false,
      "auto_generate_photo_highlights": true,
      "auto_generate_photo_scene": true,
      "file_resume": false,
      "personal_recommendation": true,
      "gmt_create": "2021-05-30T12:59:45.000+00:00",
      "gmt_modified": "2021-05-30T12:59:45.000+00:00",
      "user_id": "2a9348a769594ca45acc7c140945678f"
    }
    """
    id: int = field(default=None)
    face_ai_recognition_status: int = field(default=None)
    auto_generate_memory: int = field(default=None)
    is_sfiia_entry_hidden: bool = field(default=None)
    homepage_visibility: int = field(default=None)
    folder_cover_enable: bool = field(default=None)
    auto_generate_photo_highlights: bool = field(default=None)
    auto_generate_photo_scene: bool = field(default=None)
    file_resume: bool = field(default=None)
    personal_recommendation: bool = field(default=None)
    gmt_create: str = field(default=None)
    gmt_modified: str = field(default=None)
    user_id: str = field(default=None)
