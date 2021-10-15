# aligo

🚀🔥使用Python连接阿里云盘, 实现了官方大部分功能 👍👍

![python version](https://img.shields.io/pypi/pyversions/aligo)  [![Downloads](https://static.pepy.tech/personalized-badge/aligo?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/aligo)

```bash
pip install aligo
```

必要时可以加个 `--upgrade` 或 `-U` 参数



## 快速入门

```python
from aligo import Aligo

ali = Aligo()
user = ali.get_user()
```



## 功能列表

- [x] 扫码登录
- [x] refresh_token登录
- [x] 持久化登录
- [x] 获取用户信息
- [x] 获取云盘信息
- [x] 获取文件信息
- [x] 批量获取文件下载地址
- [x] 根据路径获取文件
- [x] 获取文件列表
- [x] 批量下载/上传文件(夹)
- [x] 秒传文件
- [x] 批量重命名/移动/复制文件(夹)
- [x] 批量收藏/取消收藏文件(夹)
- [x] 批量移动文件到回收站
- [x] 批量恢复回收站文件
- [x] 获取回收站文件列表
- [x] 搜索文件/标签
- [x] 创建官方分享，支持设置密码，有效期
- [x] 更新分享(官方)
- [x] 批量取消分享(官方)
- [x] 批量保存他人分享文件
- [x] 自定义分享，突破官方限制
- [x] 自定义分享保存
- [x] 支持自定义功能
- [x] 福利码兑换接口
- [x] ......

一般说来, 能用官方客户端实现的基本操作, 你都可以用 **aligo** 试试. 无常用功能? [反馈](https://github.com/foyoux/aligo/issues/new)



## 使用方法

**看代码提示** 或 **[旧文档](images/old_readme.md)**

![image-20210929152512759](images/image-20210929152512759.png)



## 欢迎进讨论群

<p align="center">
  <img src="images/wechat.png" alt="aligo反馈交流群"/>
</p>
