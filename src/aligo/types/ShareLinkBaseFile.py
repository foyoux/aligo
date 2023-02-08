"""..."""
from dataclasses import dataclass, field

from .BaseFile import BaseFile
from .FieldsInfo import FieldsInfo


@dataclass
class ShareLinkBaseFile(BaseFile):
    """..."""
    mime_type: str = None
    mime_extension: str = None
    revision_id: str = None
    ex_fields_info: FieldsInfo = field(default=None, repr=False)
