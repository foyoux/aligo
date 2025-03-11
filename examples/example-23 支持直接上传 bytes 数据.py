"""支持上传 bytes"""

import base64
import hashlib
from io import BytesIO
from typing import Union

import requests
from tqdm import tqdm

from aligo import (
    Aligo,
    BaseFile,
    CreateFileRequest,
    CreateFileResponse,
    Null,
    UploadPartInfo,
    GetUploadUrlRequest,
    CompleteFileRequest,
)
from aligo.core.Config import ADRIVE_V2_FILE_CREATEWITHFOLDERS
from aligo.core.Create import Create
from aligo.types.Enum import CheckNameMode


class CAligo(Aligo):

    def _pre_hash_by_bytes(
        self,
        bytes_data,
        file_size: int,
        name: str,
        parent_file_id="root",
        drive_id=None,
        check_name_mode: CheckNameMode = "auto_rename",
    ) -> CreateFileResponse:
        pre_hash = hashlib.sha1(bytes_data[:1024]).hexdigest()
        body = CreateFileRequest(
            drive_id=drive_id,
            part_info_list=self._get_part_info_list(file_size),
            parent_file_id=parent_file_id,
            name=name,
            type="file",
            check_name_mode=check_name_mode,
            size=file_size,
            pre_hash=pre_hash,
        )
        response = self.post(ADRIVE_V2_FILE_CREATEWITHFOLDERS, body=body)
        part_info = self._result(response, CreateFileResponse, [201, 409])
        return part_info

    def _get_proof_code_by_bytes(self, bytes_data) -> str:
        file_size = len(bytes_data)
        md5_int = int(
            hashlib.md5(self._auth.token.access_token.encode()).hexdigest()[:16], 16
        )
        offset = md5_int % file_size if file_size else 0
        bys = bytes_data[offset : offset + min(8, file_size - offset)]
        return base64.b64encode(bys).decode()

    def _content_hash_by_bytes(
        self,
        bytes_data,
        file_size: int,
        name: str,
        parent_file_id="root",
        drive_id=None,
        check_name_mode: CheckNameMode = "auto_rename",
    ) -> CreateFileResponse:
        content_hash = hashlib.sha1(bytes_data).hexdigest().upper()
        proof_code = self._get_proof_code_by_bytes(bytes_data)

        body = CreateFileRequest(
            drive_id=drive_id,
            part_info_list=self._get_part_info_list(file_size),
            parent_file_id=parent_file_id,
            name=name,
            type="file",
            check_name_mode=check_name_mode,
            size=file_size,
            content_hash=content_hash,
            content_hash_name="sha1",
            proof_code=proof_code,
            proof_version="v1",
        )
        response = self.post(ADRIVE_V2_FILE_CREATEWITHFOLDERS, body=body)
        if response.status_code == 400:
            body.proof_code = self._get_proof_code_by_bytes(bytes_data)
            response = self.post(ADRIVE_V2_FILE_CREATEWITHFOLDERS, body=body)
        part_info = self._result(response, CreateFileResponse, 201)
        return part_info

    def _put_data_by_bytes(
        self, bytes_data, part_info: CreateFileResponse, file_name
    ) -> Union[BaseFile, Null]:
        file_size = len(bytes_data)
        f = BytesIO(bytes_data)
        progress_bar = tqdm(
            total=file_size, unit="B", unit_scale=True, colour="#21d789"
        )
        for i in range(len(part_info.part_info_list)):
            part_info_item = part_info.part_info_list[i]
            data = f.read(self.__UPLOAD_CHUNK_SIZE)
            try:
                resp = self._session.put(data=data, url=part_info_item.upload_url)
                if resp.status_code == 403:
                    raise requests.exceptions.RequestException(
                        f"upload_url({part_info_item.upload_url}) expired"
                    )
            except requests.exceptions.RequestException:
                part_info = self.get_upload_url(
                    GetUploadUrlRequest(
                        drive_id=part_info.drive_id,
                        file_id=part_info.file_id,
                        upload_id=part_info.upload_id,
                        part_info_list=[
                            UploadPartInfo(part_number=i.part_number)
                            for i in part_info.part_info_list
                        ],
                    )
                )
                part_info_item = part_info.part_info_list[i]
                resp = self._session.put(data=data, url=part_info_item.upload_url)
            if resp.status_code == 403:
                raise "这里不对劲，请反馈：https://github.com/foyoux/aligo/issues/new"
            progress_bar.update(len(data))

        progress_bar.close()

        # complete
        complete = self.complete_file(
            CompleteFileRequest(
                drive_id=part_info.drive_id,
                file_id=part_info.file_id,
                upload_id=part_info.upload_id,
                part_info_list=part_info.part_info_list,
            )
        )
        if isinstance(complete, BaseFile):
            self._auth.log.info(f"文件上传完成 {file_name}, {len(bytes_data)=}")
        else:
            self._auth.log.info(f"文件上传失败 {file_name}, {len(bytes_data)=}")
        return complete

    def upload_file_by_bytes(
        self,
        bytes_data,
        file_name: str,
        parent_file_id: str = "root",
        drive_id: str = None,
        check_name_mode: CheckNameMode = "refuse",
    ):
        """直接上传 bytes 数据

        https://github.com/foyoux/aligo/issues/117#issuecomment-2710835893

        :param bytes_data: 字节序列
        :param file_name: 作为云盘中的文件名
        :param parent_file_id:
        :param drive_id:
        :param check_name_mode:
            'auto_rename',  # 自动重命名
            'refuse',       # 拒绝
            'overwrite',    # 覆盖
        :return:
        """
        self._auth.log.info(f"开始上传二进制数据 {len(bytes_data)=}")
        if drive_id is None:
            drive_id = self.default_drive_id
        file_size = len(bytes_data)

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
            part_info = self._pre_hash_by_bytes(
                bytes_data,
                file_size=file_size,
                name=file_name,
                parent_file_id=parent_file_id,
                drive_id=drive_id,
                check_name_mode=check_name_mode,
            )

            if part_info.code == "PreHashMatched":
                # 2. content_hash
                part_info = self._content_hash_by_bytes(
                    bytes_data,
                    file_size=file_size,
                    name=file_name,
                    parent_file_id=parent_file_id,
                    drive_id=drive_id,
                    check_name_mode=check_name_mode,
                )
                if part_info.rapid_upload:
                    self._auth.log.info(f"文件秒传成功 {file_name}, {len(bytes_data)=}")
                    return part_info
        else:
            # 2. content_hash
            part_info = self._content_hash_by_bytes(
                bytes_data,
                file_size=file_size,
                name=file_name,
                parent_file_id=parent_file_id,
                drive_id=drive_id,
                check_name_mode=check_name_mode,
            )
            if part_info.rapid_upload:
                self._auth.log.info(f"文件秒传成功 {file_name}, {len(bytes_data)=}")
                return part_info

        # exists=True
        if part_info.exist:
            self._auth.log.warning(
                f"文件已存在, 跳过 {file_name}, {len(bytes_data)=}, {part_info.file_id}"
            )
            return part_info

        return self._put_data_by_bytes(bytes_data, part_info, file_name)


if __name__ == "__main__":
    ali = CAligo()
    bytes_data = "一二三四五，上山打老虎。".encode()
    r = ali.upload_file_by_bytes(bytes_data, "test.txt")
    print(r)
