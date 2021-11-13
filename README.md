# aligo

[Wiki 帮助文档](https://github.com/foyoux/aligo/wiki)

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
    ali = Aligo()
    user = ali.get_user()  # 获取用户信息
    ll = ali.get_file_list()  # 获取网盘根目录文件列表
```



## 基本功能

- [x] 持久化登录、多帐户登录
- [x] 获取帐户、云盘（容量）等基本信息
- [x] 文件（夹）上传下载、移动复制、删除恢复、重命名、分享收藏、自定义分享（无限制）
- [x] 搜索文件/标签
- [x] 福利码兑换
- [x] 支持功能扩展

> 注：由于秒传链接的失效，自定分享信息的有效期只有4个小时。



## 欢迎加入讨论群 ❤️‍🔥

<p align="center">
  <img src="http://110.42.175.98:5512/down/LKPvT9xK2lFx?fname=/aligo/wechat.png" alt="aligo反馈交流群"/>
</p>
