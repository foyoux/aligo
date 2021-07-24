"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass(unsafe_hash=True)
class GetDefaultDriveRequest(DataClass):
    """..."""
    user_id: str
