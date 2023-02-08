"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass
class GetDefaultDriveRequest(DataClass):
    """..."""
    user_id: str
