"""发送邮件模块"""
import smtplib
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


def send_email(receiver: str, title: str, content: str, qr_data: bytes):
    """发送邮件"""
    sender = 'aligo_notify@163.com'

    msg_root = MIMEMultipart()
    msg_root['From'] = formataddr(('aligo notify', sender))
    msg_root['To'] = formataddr((receiver, receiver))
    msg_root['Subject'] = f'[阿里云盘/{title}] 扫码登录'

    msg_root.attach(
        MIMEText(f'<div align="center"><h3>{content}</h3><img style="max-width: 100%" src="cid:qrcode"></div>', 'html'))

    msg_image = MIMEImage(qr_data, 'png')
    msg_image.add_header('Content-ID', '<qrcode>')

    msg_root.attach(msg_image)

    smtp = smtplib.SMTP_SSL('smtp.163.com', 465)
    smtp.login(sender, 'IYMQTISDOZYUMUFX')
    for i in range(1, 4):
        try:
            result = smtp.sendmail(
                sender,
                [receiver],
                msg_root.as_bytes()
            )
            return result
        except smtplib.SMTPServerDisconnected:
            time.sleep(i * 3)
    raise f'邮件发送失败 {receiver}'
