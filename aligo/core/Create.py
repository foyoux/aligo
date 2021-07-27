"""todo"""
import hashlib
import math
import os
from typing import Union

import requests
from requests.adapters import HTTPAdapter

from aligo.core import *
from aligo.request import *
from aligo.response import *
from aligo.types import *

CHUNK_SIZE: int = 10485760


class Create(BaseAligo):
    """创建文件: 1.创建文件 2.上传文件 3.下载文件"""

    def create_file(self, body: CreateFileRequest) -> CreateFileResponse:
        """创建文件, 可用于上传文件"""
        response = self._post(V2_FILE_CREATE, body=body)
        return self._result(response, CreateFileResponse, status_code=201)

    def create_folder(self, body: CreateFolderRequest) -> CreateFileResponse:
        """..."""
        return self.create_file(CreateFileRequest(**body.__dict__))

    def complete_file(self, body: CompleteFileRequest) -> BaseFile:
        """当文件上传完成时调用"""
        response = self._post(V2_FILE_COMPLETE, body=body)
        return self._result(response, BaseFile)

    @staticmethod
    def _get_part_info_list(file_size: int):
        """根据文件大小, 返回 part_info_list """
        # 以10MB为一块: 10485760
        return [UploadPartInfo(part_number=i) for i in range(1, math.ceil(file_size / CHUNK_SIZE) + 1)]

    def _pre_hash(self, file_path: str, file_size: int, name: str, parent_file_id='root', drive_id=None,
                  check_name_mode: CheckNameMode = 'auto_rename') -> CreateFileResponse:
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

    def _content_hash(self, file_path: str, file_size: int, name: str, parent_file_id='root', drive_id=None,
                      check_name_mode: CheckNameMode = 'auto_rename') -> CreateFileResponse:
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
                ss = requests.session()
                # ss.mount('http://', HTTPAdapter(max_retries=5))
                ss.mount('https://', HTTPAdapter(max_retries=5))
                ss.put(data=f.read(CHUNK_SIZE), url=i.upload_url)
                # response = requests.put(data=f.read(CHUNK_SIZE), url=i.upload_url)
                # print(response)
        # complete
        return self.complete_file(CompleteFileRequest(
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
            part_info = self._content_hash(file_path=file_path, file_size=file_size, name=name,
                                           parent_file_id=parent_file_id, drive_id=drive_id,
                                           check_name_mode=check_name_mode)
            if part_info.code == 'PreHashMatched':
                # 2. content_hash
                part_info = self._content_hash(file_path=file_path, file_size=file_size, name=name,
                                               parent_file_id=parent_file_id, drive_id=drive_id,
                                               check_name_mode=check_name_mode)
                if part_info.rapid_upload:
                    return self.get_file(GetFileRequest(file_id=part_info.file_id))
            # 开始上传
            return self._put_data(file_path, part_info)

        # 2. content_hash
        part_info = self._content_hash(file_path=file_path, file_size=file_size, name=name,
                                       parent_file_id=parent_file_id, drive_id=drive_id,
                                       check_name_mode=check_name_mode)
        if part_info.rapid_upload:
            return self.get_file(GetFileRequest(file_id=part_info.file_id))
        # 开始上传
        return self._put_data(file_path, part_info)

    def create_by_content_hash(
            self,
            name: str,
            content_hash: str,
            size: int,
            parent_file_id: str = 'root',
            drive_id=None
    ) -> CreateFileResponse:
        """..."""
        return self.create_file(CreateFileRequest(
            name=name,
            content_hash=content_hash,
            size=size,
            parent_file_id=parent_file_id,
            drive_id=drive_id,
            type='file'
        ))

    @staticmethod
    def download_file(file_path: str, url: str):
        """..."""
        with requests.get(url, headers={
            'referer': 'https://www.aliyundrive.com/'
        }, stream=True) as resp:
            with open(file_path, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=int(CHUNK_SIZE / 8)):
                    f.write(chunk)
        return file_path
