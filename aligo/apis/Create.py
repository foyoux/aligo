"""todo"""

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Create(Core):
    """..."""

    def create_folder(self,
                      name: str,
                      parent_file_id: str = 'root',
                      drive_id: str = None,
                      check_name_mode: CheckNameMode = 'refuse') -> CreateFileResponse:
        """..."""
        body = CreateFolderRequest(
            name=name,
            parent_file_id=parent_file_id,
            drive_id=drive_id,
            check_name_mode=check_name_mode,
        )
        return super(Create, self).create_folder(body)
