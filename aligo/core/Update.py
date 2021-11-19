"""..."""

from dataclasses import asdict

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.types import *


class Update(BaseAligo):
    """..."""

    def update_file(self, body: UpdateFileRequest) -> BaseFile:
        """
        Update file.
        :param body: [UpdateFileRequest]
        :return: [BaseFile]

        :Example:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> new_file = ali.update_file(UpdateFileRequest(file_id='file_id', name='new_name'))
        >>> print(new_file.name)
        """
        response = self._post(V3_FILE_UPDATE, body=body)
        return self._result(response, BaseFile)

    def _core_rename_file(self, body: RenameFileRequest) -> BaseFile:
        """..."""
        return self.update_file(UpdateFileRequest(**asdict(body)))
