"""..."""
from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class Privilege(DataClass):
    """..."""
    feature_id: str = None
    feature_attr_id: str = None
    quota: int = None
