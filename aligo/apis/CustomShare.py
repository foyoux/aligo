"""自定义分享"""
import base64
import json
from typing import List

from aligo.core import *
from aligo.core.Create import Create
from aligo.core.File import File
from aligo.request import *
from aligo.types import *
from aligo.types.Enum import *


class CustomShare(Core):
    """..."""

    ALIGO_SHARE_SCHEMA = 'aligo://'

    @staticmethod
    def share_files_by_aligo(files: List[BaseFile]) -> str:
        """..."""
        result = []
        for file in files:
            result.append({
                'name': file.name,
                'content_hash': file.content_hash,
                'size': file.size
            })
        return CustomShare.ALIGO_SHARE_SCHEMA + base64.b64encode(json.dumps(result).encode()).decode()

    def __share_folder_by_aligo(self, parent_file_id: str, drive_id: str = None) -> List:
        """..."""
        result = []
        files = []
        # 1. 获取 parent_file_id 目录下文件列表
        for file in File.get_file_list(self, GetFileListRequest(parent_file_id=parent_file_id, drive_id=drive_id)):
            if file.type == 'file':
                # 2. 如果是文件, 添加到 files
                files.append(file)
                continue
            # 3. 否则是文件夹, 递归
            result.append([file.name, self.__share_folder_by_aligo(parent_file_id=file.file_id, drive_id=drive_id)])
        result.append(self.share_files_by_aligo(files))
        return result

    def share_folder_by_aligo(self, parent_file_id: str, drive_id: str = None) -> str:
        """..."""
        return CustomShare.ALIGO_SHARE_SCHEMA + base64.b64encode(
            json.dumps(
                self.__share_folder_by_aligo(parent_file_id=parent_file_id, drive_id=drive_id)).encode()).decode()

    def save_files_by_aligo(self, data: str, parent_file_id: str = 'root',
                            check_name_mode: CheckNameMode = 'auto_rename',
                            drive_id: str = None):
        """..."""
        if not data.startswith(self.ALIGO_SHARE_SCHEMA):
            self._auth.log.warning(f'这不是合法 aligo 分享协议: {data}')
            return
        result = []
        data = data[8:]
        data = json.loads(base64.b64decode(data))
        for obj in data:
            if isinstance(obj, list):
                # 创建文件夹
                folder = Create.create_folder(self, CreateFolderRequest(name=obj[0], parent_file_id=parent_file_id,
                                                                        drive_id=drive_id))
                x = self.save_files_by_aligo(obj[1], parent_file_id=folder.file_id)
                result.append((folder, x))
                continue
            # 否则为 str, 内含文件列表
            obj = obj[8:]
            obj = json.loads(base64.b64decode(obj))
            for file in obj:
                x = self.create_by_hash(name=file['name'], content_hash=file['content_hash'], size=file['size'],
                                        parent_file_id=parent_file_id, check_name_mode=check_name_mode,
                                        drive_id=drive_id)
                result.append(x)
        return result
