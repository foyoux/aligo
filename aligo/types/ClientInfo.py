"""..."""
from dataclasses import dataclass
from typing import List

from .DataClass import DataClass


@dataclass
class ClientInfo(DataClass):
    """..."""

    @dataclass
    class _File(DataClass):
        """..."""
        url: str = None
        sha512: str = None
        size: int = None

    version: str = None
    files: List[_File] = None
    path: str = None
    sha512: str = None
    releaseDate: str = None
    stagingPercentage: int = None
