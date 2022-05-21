"""..."""
from typing import List

from aligo.core import *
from aligo.response import *


class Duplicate(Core):
    """..."""

    def duplicate_list(self, drive_id: str = None) -> List[DuplicateItem]:
        """..."""
        return list(self._core_duplicate_list(drive_id))
