"""..."""

from aligo.core import *
from aligo.request import *
from aligo.types import *


class Update(Core):
    """..."""

    def rename_file(self,
                    name: str,
                    file_id: str,
                    check_name_mode: CheckNameMode = 'refuse',
                    drive_id: str = None) -> BaseFile:
        """..."""
        body = RenameFileRequest(
            name=name,
            file_id=file_id,
            check_name_mode=check_name_mode,
            drive_id=drive_id,
        )
        return super(Update, self).rename_file(body)
