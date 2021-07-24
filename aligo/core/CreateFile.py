"""todo"""
import hashlib
import math
import os
from typing import Union

import requests

from aligo.config import *
from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *

CHUNK_SIZE: int = 10485760


class CreateFile(BaseAligo):
    """创建文件: 1.创建文件 2.上串文件"""

    def _create_file(self, body: CreateFileRequest) -> CreateFileResponse:
        """创建文件, 可用于上传文件"""
        response = self._post(V2_FILE_CREATE, body=body)
        return self._result(response, CreateFileResponse, status_code=201)

    def _complete_file(self, body: CompleteFileRequest) -> BaseFile:
        """当文件上传完成时调用"""
        response = self._post(V2_FILE_COMPLETE, body=body)
        return self._result(response, BaseFile)

    @staticmethod
    def _get_part_info_list(file_size: int):
        """根据文件大小, 返回 part_info_list """
        info_list = []
        # 以10MB为一块: 10485760
        for i in range(1, math.ceil(file_size / CHUNK_SIZE) + 1):
            info_list.append(UploadPartInfo(part_number=i))
        return info_list

    def _pre_hash(self, check_name_mode, drive_id, file_path, file_size, name, parent_file_id) -> CreateFileResponse:
        with open(file_path, 'rb') as f:
            pre_hash = hashlib.sha1(f.read(1024)).hexdigest()
        body = CreateFileRequest(
            drive_id=drive_id,
            part_info_list=self._get_part_info_list(file_size),
            parent_file_id=parent_file_id,
            name=name,
            type='file',
            check_name_mode=check_name_mode,
            size=file_size,
            pre_hash=pre_hash
        )
        response = self._post(V2_FILE_CREATE, body=body)
        part_info = self._result(response, CreateFileResponse, [201, 409])
        return part_info

    def _content_hash(self, check_name_mode, drive_id, file_path, file_size, name,
                      parent_file_id) -> CreateFileResponse:
        with open(file_path, 'rb') as f:
            content_hash = hashlib.sha1(f.read()).hexdigest().upper()
        body = CreateFileRequest(
            drive_id=drive_id,
            part_info_list=self._get_part_info_list(file_size),
            parent_file_id=parent_file_id,
            name=name,
            type='file',
            check_name_mode=check_name_mode,
            size=file_size,
            content_hash=content_hash,
            content_hash_name="sha1"
        )
        response = self._post(V2_FILE_CREATE, body=body)
        part_info = self._result(response, CreateFileResponse, 201)
        return part_info

    def _put_data(self, file_path: str, part_info: CreateFileResponse) -> Union[BaseFile, Null]:
        """上传数据"""
        with open(file_path, 'rb') as f:
            for i in part_info.part_info_list:
                # 不能使用 self._session.put
                # requests.put(data=f.read(CHUNK_SIZE), url=i.upload_url)
                response = requests.put(data=f.read(CHUNK_SIZE), url=i.upload_url)
                print(response)
        # complete
        return self._complete_file(CompleteFileRequest(
            drive_id=part_info.drive_id,
            file_id=part_info.file_id,
            upload_id=part_info.upload_id,
            part_info_list=part_info.part_info_list
        ))

    def upload_file(
            self,
            file_path: str,
            parent_file_id: str = 'root',
            name: str = None,
            drive_id: str = None,
            check_name_mode: CheckNameMode = "auto_rename"
    ) -> BaseFile:
        """..."""
        if name is None:
            name = os.path.basename(file_path)

        if drive_id is None:
            drive_id = self.default_drive_id

        file_size = os.path.getsize(file_path)
        if file_size > 1024:  # 1kB
            # 1. pre_hash
            part_info = self._pre_hash(check_name_mode, drive_id, file_path, file_size, name, parent_file_id)
            if part_info.code == 'PreHashMatched':
                part_info = self._content_hash(check_name_mode, drive_id, file_path, file_size, name, parent_file_id)
                if part_info.rapid_upload:
                    return self.get_file(GetFileRequest(file_id=part_info.file_id))
            # 开始上传
            return self._put_data(file_path, part_info)

        # 2. content_hash
        part_info = self._content_hash(check_name_mode, drive_id, file_path, file_size, name, parent_file_id)
        if part_info.rapid_upload:
            return self.get_file(GetFileRequest(file_id=part_info.file_id))
        # 开始上传
        return self._put_data(file_path, part_info)

    # def _proof_code(self, file_path: str) -> str:
    #     """计算pre_hash"""
    #     with open(file_path, 'rb') as f:
    #         n1 = int(md5(self._token.access_token.encode()).hexdigest()[:16], 16)
    #         file_size = os.path.getsize(file_path)
    #         n3 = n1 % file_size
    #         f.seek(n3)
    #         bys = f.read(min(8, file_size - n3))
    #         return base64.b64encode(bys).decode()

    # def upload_by_content_hash(
    #         self,
    #         name: str,
    #         content_hash: str,
    #         size: int,
    #         parent_file_id: str = 'root',
    #         drive_id=None
    # ) -> CreateFileResponse:
    #     """..."""
    #     # 无需缓存, 无需处理drive_id
    #     return self._create_file(CreateFileRequest(
    #         name=name,
    #         content_hash=content_hash,
    #         size=size,
    #         parent_file_id=parent_file_id,
    #         drive_id=drive_id,
    #         type='file'
    #     ))

    # def share_by_content_hash(self, content_hash: str, size: int, name: str = None, password: str = None) -> str:
    #     """..."""
    #     raise NotImplementedError
