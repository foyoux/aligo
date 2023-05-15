"""..."""

from dataclasses import dataclass

from .DataClass import DataClass


@dataclass
class EMailConfig(DataClass):
    """邮箱配置"""
    email: str  # 接收邮件的邮箱
    host: str  # 示例值 'smtp.163.com'
    port: int  # 示例值 465
    user: str  # 示例值 'aligo_notify@163.com'
    password: str  # 示例值 'IFMXTIOSDYZUMUYW'
    content: str = ''  # 附加内容
