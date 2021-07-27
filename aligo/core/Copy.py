"""..."""
from typing import Iterator

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Copy(BaseAligo):
    """..."""
    MAX_COPY_COUNT = 100

    def copy_file(self, body: CopyFileRequest) -> CopyFileResponse:
        """..."""
        response = self._post(V2_FILE_COPY, body=body)
        return self._result(response, CopyFileResponse, [201, 202])

    def batch_copy_files(self, body: BatchCopyFilesRequest) -> Iterator[BatchResponse]:
        """..."""
        if body.drive_id is None:
            body.drive_id = self.default_drive_id
        for file_id_list in self._list_split(body.file_id_list, self.MAX_COPY_COUNT):
            response = self._post(V2_BATCH, body={
                "requests": [
                    {
                        "body": {
                            "drive_id": body.drive_id,
                            "file_id": file_id,
                            "to_parent_file_id": body.to_parent_file_id,
                            "overwrite": body.overwrite,
                            "auto_rename": body.auto_rename
                        },
                        "headers": {"Content-Type": "application/json"},
                        "id": file_id,
                        "method": "POST",
                        "url": "/file/copy"
                    } for file_id in file_id_list
                ],
                "resource": "file"
            })

            if response.status_code != 200:
                yield Null(response)
                return

            for batch in response.json()['responses']:
                yield BatchResponse(**batch)

# @overload
# def copy_file(self, body: CopyFileRequest) -> CopyFileResponse:
#     """..."""
#     ...
#
# @overload
# def copy_file(self, file_id: str,
#               to_parent_file_id: str = 'root',
#               drive_id: str = None,
#               to_drive_id: str = None, ) -> CopyFileResponse:
#     """..."""
#     ...
#
# def copy_file(
#         self,
#         body: CopyFileRequest = None,
#         file_id: str = None,
#         to_parent_file_id: str = 'root',
#         drive_id: str = None,
#         to_drive_id: str = None,
# ) -> CopyFileResponse:
#     """..."""
#     # CopyFileRequest的to_parent_file_id已具有'root'默认值
#     # if body.to_parent_file_id is None:
#     #     body.to_parent_file_id = 'root'
#     if body is None:
#         body = CopyFileRequest(
#             file_id=file_id,
#             to_parent_file_id=to_parent_file_id,
#             drive_id=drive_id,
#             to_drive_id=to_drive_id
#         )
#     if body.drive_id is None:
#         body.drive_id = self.default_drive_id
#     if body.to_drive_id is None:
#         body.to_drive_id = self.default_drive_id
#     response = self._post(V2_FILE_COPY, body=body)
#     return self._result(response, CopyFileResponse, 202)
