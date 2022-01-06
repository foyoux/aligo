# aligo

[Wiki 帮助文档](https://github.com/foyoux/aligo/wiki)

[examples](https://github.com/foyoux/aligo/tree/main/examples)

🚀🔥 用Python连接阿里云盘 👍👍

**aligo** 是一个操作阿里云盘的 **Python** 库

提供简单易用的API接口，可以让你轻松通过代码与阿里云盘进行交互。


[![python version](https://img.shields.io/pypi/pyversions/aligo)](https://pypi.org/project/aligo/)  [![Downloads](https://static.pepy.tech/personalized-badge/aligo?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/aligo)

```bash
pip install --upgrade aligo
```



## 快速入门

```python
"""快速入门"""
from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()  # 第一次使用，会弹出二维码，供扫描登录
    user = ali.get_user()  # 获取用户信息
    ll = ali.get_file_list()  # 获取网盘根目录文件列表
    # 遍历文件列表
    for file in ll:
        print(file.file_id, file.name, file.type)
```



## 基本功能

> 完全的代码提示

- [x] 持久化登录、多帐户登录
- [x] 获取帐户、云盘（容量）等基本信息
- [x] 文件（夹）上传下载、移动复制、删除恢复、重命名、分享收藏、自定义分享（无限制）
- [x] 搜索文件/标签
- [x] 福利码兑换
- [x] 支持功能扩展
- [x] 文件夹同步

> 注：由于秒传链接的失效，自定分享信息的有效期只有4个小时。



## API 概览

> 详情请参考源码（在IDE中点进去）：源码中有详细的文档注释和用法示例



### 文件（夹）相关

- 创建文件夹：`create_folder`

- 重命名文件（夹）

  - `rename_file`: 重命名文件（夹）

  - `batch_rename_files`: 批量重命名文件（夹）

- 移动文件（夹）

  - `move_file`: 移动文件（夹）

  - `batch_move_files`: 批量移动文件（夹）

- 复制文件（夹）

  - `copy_file`: 复制文件（夹）

  - `batch_copy_files`: 批量复制文件（夹）

- 获取文件（夹）

  - `get_file`: 获取文件（夹）
  - `batch_get_files`: 批量获取文件（夹）
  - `get_file_by_path`: 根据路径获取文件（夹）

- 获取文件列表: `get_file_list`

- 其他

  - `get_path`: 获取文件（夹）路径信息



### 收藏相关

- `starred_file`: 收藏和取消收藏 文件（夹）

- `batch_star_files`: 批量收藏和取消收藏 文件（夹）



### 分享相关

- `get_share_list`: 获取分享列表
- 分享文件（夹）
  - `share_file`: （批量）分享文件（夹）
- 取消分享文件（夹）
  - `cancel_share`: 取消分享
  - `batch_cancel_share`: 批量取消分享
- `update_share`: 更新分享
- `get_share_info`: 获取分享信息
- `get_share_token`: 获取分享 token
- `get_share_file`: 获取分享文件（夹）
- `get_share_file_list`: 获取分享文件列表
- `share_file_saveto_drive`: 保存分享文件（夹）
- `batch_share_file_saveto_drive`: 批量保存分享文件（夹）
- `get_share_link_download_url`: 



### 自定义分享

- `share_files_by_aligo`: 批量分享文件
- `share_folder_by_aligo`: 分享文件夹
- `save_files_by_aligo`：保存自定义分享



### 回收站相关

- `get_recyclebin_list`: 获取回收站文件列表

- 移动文件（夹）至回收站：*不提供彻底删除的接口，如需使用，请参考自定义功能*

  - `move_file_to_trash`: 移动文件（夹）到回收站

  - `batch_move_to_trash`: 批量移动文件（夹）到回收站

- 从回收站恢复文件（夹）

  - `restore_file`: 恢复回收站文件（夹）

  - `batch_restore_files`: 批量恢复回收站文件（夹）



### 下载相关

- `download_file`: 下载文件
- `download_files`: 批量下载文件
- `download_folder`: 下载文件夹
- 其他
  - `get_download_url`: 获取文件下载地址（一般不直接使用）
  - `batch_download_url`: 批量获取文件下载地址（一般不直接使用）



### 上传相关

- `upload_file`: 上传文件
- `upload_files`: 批量上传文件
- `upload_folder`: 上传文件夹



### 其他

- `sync_folder`: 文件夹同步



## 欢迎加入讨论群 ❤️‍🔥

<p align="center">
  <img src="http://110.42.175.98:5512/down/LKPvT9xK2lFx?fname=/aligo/wechat.png" alt="aligo反馈交流群"/>
</p>
