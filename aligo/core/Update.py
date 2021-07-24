"""..."""

from aligo.config import *
from aligo.core import *
from aligo.request import *
from aligo.types import *


class Update(BaseAligo):
    """..."""

    def update_file(self, body: UpdateFileRequest) -> BaseFile:
        """..."""
        response = self._post(V2_FILE_UPDATE, body=body)
        return self._result(response, BaseFile)

    # @overload
    # def rename_name(self, body: str, new_name: str, drive_id: str = None) -> BaseFile:
    #     """..."""
    #     pass
    #
    # @overload
    # def rename_name(self, body: BaseFile, new_name: str, drive_id: str = None) -> BaseFile:
    #     """..."""
    #     pass
    #
    # def rename_name(self, body: Union[str, BaseFile], new_name: str, drive_id: str = None) -> BaseFile:
    #     """..."""
    #     if isinstance(body, BaseFile):
    #         body = body.file_id
    #     return self.update_file(UpdateFileRequest(file_id=body, name=new_name, drive_id=drive_id))
