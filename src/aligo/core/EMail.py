"""发送邮件模块"""
import smtplib
import ssl
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


def send_email(
        receiver: str, title: str, content: str, qr_data: bytes,
        email_user: str, email_password: str, email_host: str, email_port: int,
):
    """发送邮件"""
    msg_root = MIMEMultipart()
    msg_root['From'] = formataddr(('aligo notify', email_user))
    msg_root['To'] = formataddr((receiver, receiver))
    msg_root['Subject'] = f'[阿里云盘/{title}] 扫码登录'

    msg_root.attach(
        MIMEText(f'<div align="center"><h3>{content}</h3><img style="max-width: 100%" src="cid:qrcode"></div>', 'html'))

    msg_image = MIMEImage(qr_data, 'png')
    msg_image.add_header('Content-ID', '<qrcode>')

    msg_root.attach(msg_image)

    try:
        smtp = smtplib.SMTP_SSL(email_host, email_port)
    except ssl.SSLError:
        smtp = smtplib.SMTP(email_host, email_port)
    smtp.login(email_user, email_password)
    for i in range(1, 4):
        try:
            result = smtp.sendmail(
                email_user,
                [receiver],
                msg_root.as_bytes()
            )
            return result
        except smtplib.SMTPServerDisconnected:
            time.sleep(i * 3)
    raise f'邮件发送失败 {receiver}'
