# aligo

🚀🔥使用Python连接阿里云盘, 实现了官方大部分功能 👍👍

![python version](https://img.shields.io/pypi/pyversions/aligo)  [![Downloads](https://static.pepy.tech/personalized-badge/aligo?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/aligo)

```bash
pip install aligo
```

必要时可以加个 `--upgrade` 或 `-U` 参数

<br />

[Wiki 帮助文档](https://github.com/foyoux/aligo/wiki)

<br />

## 欢迎有需要的小伙伴支持支持（临时推广）

[腾讯云双11爆款云产品](https://cloud.tencent.com/act/double11?spread_hash_key=a30261e00f34c17dfdbcf519d9004ba3&cps_key=032c6f7348a376a40e9f78ba2aa25a4f) 

[腾讯云无忧购云服务器](https://cloud.tencent.com/act/lighthouse) (无推广, 用自己的小号分享, 大号助力, 领取30元无门槛续费优惠券, 每天一次. 30可续费无忧服务器两个月)

[![新客专属福利](http://110.42.175.98:5512/down/LKPvT9xK2lFx?fname=/tencent-cps/新用户.jpg)](https://curl.qcloud.com/9uB7iZrb)

[![首单限时](http://110.42.175.98:5512/down/LKPvT9xK2lFx?fname=/tencent-cps/首单限时.jpg)](https://curl.qcloud.com/07sf8CHP)

[![全球购](http://110.42.175.98:5512/down/LKPvT9xK2lFx?fname=/tencent-cps/全球购.jpg)](https://curl.qcloud.com/jUXcFNPg)

[![云数据库](http://110.42.175.98:5512/down/LKPvT9xK2lFx?fname=/tencent-cps/云数据库.jpg)](https://curl.qcloud.com/YdssIVV6)

<br />

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

![image-20210929152512759](http://110.42.175.98:5512/down/LKPvT9xK2lFx?fname=/aligo/image-20210929152512759.png)



## 欢迎进讨论群

<p align="center">
  <img src="http://110.42.175.98:5512/down/LKPvT9xK2lFx?fname=/aligo/wechat.png" alt="aligo反馈交流群"/>
</p>
