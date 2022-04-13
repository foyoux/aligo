"""..."""

from aligo.core import Core
from aligo.request import ArchiveUncompressRequest, ArchiveStatusRequest
from aligo.response import ArchiveUncompressResponse, ArchiveStatusResponse
from aligo.types.Enum import ArchiveType


class Compress(Core):
    """..."""

    def archive_uncompress(
            self, file_id: str,
            target_file_id: str = 'root',
            archive_type: ArchiveType = 'zip',
            drive_id: str = None,
            target_drive_id: str = None
    ) -> ArchiveUncompressResponse:
        """创建在线解压缩任务"""
        if target_drive_id is None:
            target_drive_id = self.default_drive_id
        body = ArchiveUncompressRequest(
            file_id, target_file_id, archive_type, drive_id, target_drive_id
        )
        return self._core_archive_uncompress(body)

    def archive_status(
            self,
            file_id: str,
            task_id: str,
            drive_id: str = None
    ) -> ArchiveStatusResponse:
        """..."""
        body = ArchiveStatusRequest(
            file_id, task_id, drive_id
        )
        return self._core_archive_status(body)
