"""..."""
from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class UploadPartInfo(DataClass):
    """
    {
        "part_number": 1
    }
    """
    etag: str = None
    part_number: int = None
    part_size: int = None
    upload_url: str = None
    internal_upload_url: str = None
    content_type: str = None
    upload_form_info: str = None
    internal_upload_form_info: str = None
