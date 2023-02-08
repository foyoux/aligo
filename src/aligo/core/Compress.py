"""..."""
from aligo.core.Config import V2_ARCHIVE_UNCOMPRESS, V2_ARCHIVE_STATUS
from aligo.request import ArchiveUncompressRequest, ArchiveStatusRequest
from aligo.response import ArchiveUncompressResponse, ArchiveStatusResponse
from .BaseAligo import BaseAligo


class Compress(BaseAligo):
    """..."""

    def _core_archive_uncompress(self, body: ArchiveUncompressRequest) -> ArchiveUncompressResponse:
        """新建在线解压缩任务"""
        if body.target_drive_id is None:
            body.target_drive_id = self.default_drive_id
        response = self._post(V2_ARCHIVE_UNCOMPRESS, body=body)
        return self._result(response, ArchiveUncompressResponse, status_code=202)

    def _core_archive_status(self, body: ArchiveStatusRequest) -> ArchiveStatusResponse:
        """获取在线解压缩任务状态"""
        response = self._post(V2_ARCHIVE_STATUS, body=body)
        return self._result(response, ArchiveStatusResponse)
