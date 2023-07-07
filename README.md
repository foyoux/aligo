# aligo

🚀🔥 简单、易用、可扩展的阿里云盘 API 接口库 👍👍

[wiki 文档](https://github.com/foyoux/aligo/wiki) + [examples](https://github.com/foyoux/aligo/tree/main/examples)

> 文档写得很简单，详情请查看 代码提示 + 文档注释
> 
> 有任何疑问 请 [issue](https://github.com/foyoux/aligo/issues/new?assignees=&labels=&template=bug_report.md&title=)
> 或 加入 **aligo交流反馈群** （群二维码在底部）

[![python version](https://img.shields.io/pypi/pyversions/aligo)](https://pypi.org/project/aligo/)  [![Downloads](https://static.pepy.tech/personalized-badge/aligo?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/aligo)

```sh
pip install -U aligo
pip install git+https://github.com/foyoux/aligo.git
```

## 快速入门

```python
"""快速入门"""
from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()  # 第一次使用，会弹出二维码，供扫描登录
    
    user = ali.get_user()  # 获取用户信息
    print(user.user_name, user.nick_name, user.phone)  # 打印用户信息
    
    ll = ali.get_file_list()  # 获取网盘根目录文件列表
    for file in ll:  # 遍历文件列表
        print(file.file_id, file.name, file.type)  # 打印文件信息
```

https://user-images.githubusercontent.com/35125624/150529002-c2f1b80b-fb11-4e0a-9fd7-6f57f678ccf5.mp4

## 基本功能

- [x] 完全的代码提示
- [x] 持久化登录、多帐户登录
- [x] 福利码兑换
- [x] 文件夹同步
- [x] 在线解压缩
- [x] 支持功能扩展
- [x] 搜索文件/标签
- [x] 获取重复文件列表
- [x] 文件（夹）重命名
- [x] 文件（夹）上传下载
- [x] 文件（夹）移动复制
- [x] 文件（夹）删除恢复
- [x] 获取文档在线预览接口
- [x] 文件（夹）分享 保存 收藏
- [x] 文件（夹）自定义分享（无限制）
- [x] 获取帐户、云盘（容量）等基本信息
- [x] 相册 创建 删除 修改 添加文件 获取文件

更多接口功能，请安装最新版尝试

欢迎大家发起 [新功能请求](https://github.com/foyoux/aligo/issues/new?assignees=&labels=&template=feature_request.md&title=)

> **温馨提示：**
>   1. 由于秒传链接的失效，自定分享信息的有效期只有4个小时。
>   2. 阿里云盘不同于其他网盘或系统，其定位文件不是基于文件名（路径），而是通过 `file_id`，这才是唯一定位文件的方式，**aligo** 中提供了简便函数 `get_file_by_path`/`get_folder_by_path`，通过网盘路径获取文件对象，通过 其上的 `file_id` 属性即可获取所需文件标识。但不建议频繁使用此方法，因为内部是通过 `get_file_list` 遍历得到的。
>   3. 在保存超大分享时（分享中的文件特别多），执行保存全部的方法 - `share_file_save_all_to_drive`，它会立刻执行完毕，但是文件不会立刻被保存到网盘中，阿里云盘服务器会帮你在后台陆续将所有文件存到你的网盘中；所有当你使用 `share_file_save_all_to_drive` 保存超大分享时，却只看到一部分文件时，不用疑惑，这是正常情况。

## 登录
### 网页扫码登录

```python
from aligo import Aligo

# 提供 port 参数即可, 之后打开浏览器访问 http://<YOUR_IP>:<port>
ali = Aligo(port=8080)
```


### 发送登录二维码到邮箱（推荐）

**最佳实践**：建议将邮箱绑定到微信，这样能实时收到提醒，登录过期后也可以第一时间收到登录请求。

```python
from aligo import Aligo, EMailConfig

if __name__ == '__main__':
    email_config = EMailConfig(
        email='<接收登录邮件的邮箱地址>',
        # 自配邮箱
        user='',
        password='',
        host='',
        port=0,
    )
    ali = Aligo(email=email_config)
```

## 如何彻底删除文件？
> 无需先移动文件到回收站

此功能太危险，**aligo** 未直接提供。不过 [这里](https://github.com/foyoux/aligo/wiki/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%8A%9F%E8%83%BD---%E5%BD%BB%E5%BA%95%E5%88%A0%E9%99%A4%E6%96%87%E4%BB%B6) 扩展了该功能，请小心使用！


## 关于扩展功能

一般步骤：

    1. 使用浏览器或其他抓包工具，观察通信过程；
    2. 获取 url/path + 请求体；
    3. 继承 `Aligo`, 使用现有的方法 `self._post` 等，进行发送请求；
    
会自动维护 **token**, 你只需关注如何发送请求即可

[扩展功能举栗🌰 - 配有视频和代码](https://github.com/foyoux/aligo/issues/24)


## 不慎泄露 refresh_token ?

虽然官方提供下线功能，但还是要 马上修改密码

今天无意中发现，之前使用 aligo 登录的会在登录设备列表中，但今天发现再使用 aligo 登录，已经不会出现在登录设备列表中，我也不知道为什么

今天把除我手机之外的所有设备下线后，包括 Chrome 和 aligo 登录的，但并没有失效，所有的 token 和 refresh_token 还是可以使用

所以还是得 -> 必须马上修改密码！必须马上修改密码！必须马上修改密码！


## 声明

此项目仅供学习交流，若有不妥之处，侵联必删。

---

<table align="center">
    <thead align="center">
    <tr>
        <td><h2>❤️‍🔥欢迎加入🤝🏼</h2></td>
    </tr>
    </thead>
    <tbody align="center">
    <tr>
        <td><img src="http://110.42.175.98/github/aligo/wechat.jpg#qrcode" alt="aligo反馈交流群"/></td>
    </tr>
    </tbody>
    <tfoot align="center">
    <tr>
        <td>😃 二维码会保持更新 😜</td>
    </tr>
    </tfoot>
</table>
