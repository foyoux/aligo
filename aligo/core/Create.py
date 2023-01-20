"""创建文件夹, 上传文件等"""
import base64
import hashlib
import math
import os
from dataclasses import asdict
from typing import Union, List

import requests.exceptions
from tqdm import tqdm

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *
from aligo.types import *
from aligo.types.Enum import *


class Create(BaseAligo):
    """创建文件: 1.创建文件 2.上传文件 3.下载文件"""
    # 控制内存消耗 100M 左右，但默认单文件上传只支持 1T，如需更大，手动 调节 Create._UPLOAD_CHUNK_SIZE 的值
    _UPLOAD_CHUNK_SIZE: int = None
    __UPLOAD_CHUNK_SIZE: int = 10485760  # 10 MB

    def create_file(self, body: CreateFileRequest) -> CreateFileResponse:
        """
        创建文件, 可用于上传文件
        :param body: [CreateFileRequest]
        :return: [CreateFileResponse]

        :Example:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.create_file(CreateFileRequest(name='test.txt', parent_file_id='root', type='file', size=1024))
        >>> print(result.file_id)
        """
        response = self._post(ADRIVE_V2_FILE_CREATEWITHFOLDERS, body=body)
        return self._result(response, CreateFileResponse, status_code=201)

    def _core_create_folder(self, body: CreateFolderRequest) -> CreateFileResponse:
        """..."""
        return self.create_file(CreateFileRequest(**asdict(body)))

    def complete_file(self, body: CompleteFileRequest) -> BaseFile:
        """
        完成文件上传 当文件上传完成时调用
        :param body: [CompleteFileRequest]
        :return: [BaseFile]

        :Example:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> result = ali.complete_file(CompleteFileRequest(file_id='file_id', part_info_list=[UploadPartInfo(part_number=1)]))
        >>> print(result.file_id)
        """
        response = self._post(V2_FILE_COMPLETE, body=body)
        return self._result(response, BaseFile)

    @staticmethod
    def _get_part_info_list(file_size: int) -> List[UploadPartInfo]:
        """根据文件大小, 返回 part_info_list """
        # 以10MB为一块: 10485760
        return [UploadPartInfo(part_number=i) for i in range(1, math.ceil(file_size / Create.__UPLOAD_CHUNK_SIZE) + 1)]

    def _pre_hash(self, file_path: str, file_size: int, name: str, parent_file_id='root', drive_id=None,
                  check_name_mode: CheckNameMode = 'auto_rename') -> CreateFileResponse:
        with open(file_path, 'rb') as f:
            # prehash 必须是前 1024 个字节的 SHA1
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
        response = self._post(ADRIVE_V2_FILE_CREATEWITHFOLDERS, body=body)
        part_info = self._result(response, CreateFileResponse, [201, 409])
        return part_info

    def _get_proof_code(self, file_path: str, file_size: int) -> str:
        """计算proof_code"""
        md5_int = int(hashlib.md5(self._auth.token.access_token.encode()).hexdigest()[:16], 16)
        # file_size = os.path.getsize(file_path)
        offset = md5_int % file_size if file_size else 0
        if file_path.startswith('http'):
            # noinspection PyProtectedMember
            bys = self._session.get(file_path, headers={
                'Range': f'bytes={offset}-{min(8 + offset, file_size) - 1}'
            }).content
        else:
            with open(file_path, 'rb') as file:
                file.seek(offset)
                bys = file.read(min(8, file_size - offset))
        return base64.b64encode(bys).decode()

    def _content_hash(self, file_path: str, file_size: int, name: str, parent_file_id='root', drive_id=None,
                      check_name_mode: CheckNameMode = 'auto_rename') -> CreateFileResponse:

        content_hash = hashlib.sha1()

        with open(file_path, 'rb') as f:
            while True:
                segment = f.read(self.__UPLOAD_CHUNK_SIZE)
                if not segment:
                    break
                content_hash.update(segment)

        content_hash = content_hash.hexdigest().upper()

        proof_code = self._get_proof_code(file_path, file_size)

        body = CreateFileRequest(
            drive_id=drive_id,
            part_info_list=self._get_part_info_list(file_size),
            parent_file_id=parent_file_id,
            name=name,
            type='file',
            check_name_mode=check_name_mode,
            size=file_size,
            content_hash=content_hash,
            content_hash_name="sha1",
            proof_code=proof_code,
            proof_version='v1'
        )
        response = self._post(ADRIVE_V2_FILE_CREATEWITHFOLDERS, body=body)
        # AttributeError: 'Null' object has no attribute 'rapid_upload'
        if response.status_code == 400:
            body.proof_code = self._get_proof_code(file_path, file_size)
            response = self._post(ADRIVE_V2_FILE_CREATEWITHFOLDERS, body=body)
        part_info = self._result(response, CreateFileResponse, 201)
        return part_info

    def get_upload_url(self, body: GetUploadUrlRequest) -> GetUploadUrlResponse:
        """
        获取上传文件的url
        :param body: [GetUploadUrlRequest]
        :return: [GetUploadUrlResponse]
        """
        response = self._post(V2_FILE_GET_UPLOAD_URL, body=body)
        return self._result(response, GetUploadUrlResponse)

    def _put_data(self, file_path: str, part_info: CreateFileResponse, file_size: int) -> Union[BaseFile, Null]:
        """上传数据"""
        with open(file_path, 'rb') as f:
            progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, colour='#21d789')
            for i in range(len(part_info.part_info_list)):
                part_info_item = part_info.part_info_list[i]
                data = f.read(Create.__UPLOAD_CHUNK_SIZE)
                try:
                    resp = self._session.put(data=data, url=part_info_item.upload_url)
                    if resp.status_code == 403:
                        raise requests.exceptions.RequestException(f'upload_url({part_info_item.upload_url}) expired')
                except requests.exceptions.RequestException:
                    part_info = self.get_upload_url(GetUploadUrlRequest(
                        drive_id=part_info.drive_id,
                        file_id=part_info.file_id,
                        upload_id=part_info.upload_id,
                        part_info_list=[UploadPartInfo(part_number=i.part_number) for i in part_info.part_info_list]
                    ))
                    part_info_item = part_info.part_info_list[i]
                    resp = self._session.put(data=data, url=part_info_item.upload_url)
                if resp.status_code == 403:
                    raise '这里不对劲，请反馈：https://github.com/foyoux/aligo/issues/new'
                progress_bar.update(len(data))

        progress_bar.close()

        # complete
        complete = self.complete_file(CompleteFileRequest(
            drive_id=part_info.drive_id,
            file_id=part_info.file_id,
            upload_id=part_info.upload_id,
            part_info_list=part_info.part_info_list
        ))
        if isinstance(complete, BaseFile):
            self._auth.log.info(f'文件上传完成 {file_path}')
        else:
            self._auth.log.info(f'文件上传失败 {file_path}')
        return complete

    def upload_file(
            self,
            file_path: str,
            parent_file_id: str = 'root',
            name: str = None,
            drive_id: str = None,
            check_name_mode: CheckNameMode = "auto_rename"
    ) -> Union[BaseFile, CreateFileResponse]:
        """
        上传文件
        :param file_path: [str] 文件路径
        :param parent_file_id: [str] 父文件夹id
        :param name: [str] 文件名
        :param drive_id: [str] 父文件夹所在的网盘id
        :param check_name_mode: [CheckNameMode] 文件名检查模式, 默认为auto_rename
        :return: [Union[BaseFile, CreateFileResponse]]

        :Example:
        >>> from aligo import Aligo
        >>> ali = Aligo()
        >>> up_file = ali.upload_file('/Users/aligo/Desktop/test.txt')
        >>> print(up_file)
        """
        self._auth.log.info(f'开始上传文件 {file_path}')
        file_path = os.path.abspath(file_path)
        if name is None:
            name = os.path.basename(file_path)

        if drive_id is None:
            drive_id = self.default_drive_id

        file_size = os.path.getsize(file_path)

        # 动态调整 _UPLOAD_CHUNK_SIZE
        if Create._UPLOAD_CHUNK_SIZE is None:
            if file_size < 104857600000:  # (1024 * 1024 * 10) * 10000
                Create.__UPLOAD_CHUNK_SIZE = 10485760  # (1024 * 1024 * 10) => 10 MB
            else:
                Create.__UPLOAD_CHUNK_SIZE = 268435456  # 256 MB
        else:
            if file_size < Create._UPLOAD_CHUNK_SIZE * 10000:
                Create.__UPLOAD_CHUNK_SIZE = Create._UPLOAD_CHUNK_SIZE
            else:
                Create.__UPLOAD_CHUNK_SIZE = 268435456  # 256 MB

        if file_size > 1024:  # 1kB
            # 1. pre_hash
            part_info = self._pre_hash(file_path=file_path, file_size=file_size, name=name,
                                       parent_file_id=parent_file_id, drive_id=drive_id,
                                       check_name_mode=check_name_mode)

            if part_info.code == 'PreHashMatched':
                # 2. content_hash
                part_info = self._content_hash(file_path=file_path, file_size=file_size, name=name,
                                               parent_file_id=parent_file_id, drive_id=drive_id,
                                               check_name_mode=check_name_mode)
                if part_info.rapid_upload:
                    self._auth.log.info(f'文件秒传成功 {file_path}')
                    # return self.get_file(GetFileRequest(file_id=part_info.file_id))
                    return part_info
            # 开始上传
            # return self._put_data(file_path, part_info, file_size)
        else:
            # 2. content_hash
            part_info = self._content_hash(file_path=file_path, file_size=file_size, name=name,
                                           parent_file_id=parent_file_id, drive_id=drive_id,
                                           check_name_mode=check_name_mode)
            if part_info.rapid_upload:
                self._auth.log.info(f'文件秒传成功 {file_path}')
                # return self.get_file(GetFileRequest(file_id=part_info.file_id))
                return part_info
            # 开始上传
            # return self._put_data(file_path, part_info, file_size)

        # exists=True
        if part_info.exist:
            self._auth.log.warning(f'文件已存在, 跳过 {file_path} {part_info.file_id}')
            # return self.get_file(GetFileRequest(file_id=part_info.file_id))
            return part_info

        return self._put_data(file_path, part_info, file_size)

    def create_by_hash(
            self,
            name: str,
            content_hash: str,
            size: int,
            url: str,
            parent_file_id: str = 'root',
            check_name_mode: CheckNameMode = 'auto_rename',
            drive_id: str = None
    ) -> CreateFileResponse:
        """
        文件秒传
        :param name: [必填] 文件名 随意
        :param content_hash: [必填] 文件hash
        :param size: [必填] 文件大小
        :param url: [必填] 文件下载地址(支持断点续传) 或 本地路径
        :param parent_file_id: [选填] 父文件夹id
        :param check_name_mode: [选填] 文件名检查模式, 默认为auto_rename
        :param drive_id: [选填] 网盘id
        :return: [CreateFileResponse]
        """
        self._auth.log.info(f'开始秒传 {name} {content_hash} {size}')
        proof_code = self._get_proof_code(url, size)
        body = CreateFileRequest(
            name=name,
            content_hash=content_hash,
            size=size,
            parent_file_id=parent_file_id,
            drive_id=drive_id,
            type='file',
            content_hash_name='sha1',
            check_name_mode=check_name_mode,
            proof_code=proof_code,
            proof_version='v1'
        )
        response = self._post(ADRIVE_V2_FILE_CREATEWITHFOLDERS, body=body)
        return self._result(response, CreateFileResponse, 201)
