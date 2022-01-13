"""..."""
from dataclasses import dataclass, field

from .BaseFile import BaseFile
from .DataClass import DataClass


@dataclass
class FieldsInfo(DataClass):
    """..."""
    image_count: int = 0


@dataclass
class ShareLinkBaseFile(BaseFile):
    """..."""
    mime_type: str = None
    mime_extension: str = None
    revision_id: str = None
    ex_fields_info: FieldsInfo = field(default=None, repr=False)
