"""..."""

from dataclasses import asdict

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.types import *


class Update(BaseAligo):
    """..."""

    def update_file(self, body: UpdateFileRequest) -> BaseFile:
        """..."""
        response = self._post(V2_FILE_UPDATE, body=body)
        return self._result(response, BaseFile)

    def rename_file(self, body: RenameFileRequest) -> BaseFile:
        """..."""
        return self.update_file(UpdateFileRequest(**asdict(body)))
