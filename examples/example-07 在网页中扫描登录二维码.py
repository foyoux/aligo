"""..."""
import os
import tempfile
from http.server import BaseHTTPRequestHandler, HTTPServer

import qrcode

from aligo import Aligo


class MyServer(BaseHTTPRequestHandler):
    """..."""

    def do_GET(self):
        """..."""
        if self.path == '/':
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(
                f"""
                    <html>
                        <head>
                            <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
                            <title>登录阿里云盘</title>
                        </head>
                        <body>
                            <p align="center"><img src="/login.png"></p>
                        </body>
                    </html>
                """, 'utf8'
            ))
        elif self.path == '/login.png':
            self.send_response(200)
            self.send_header("content-type", "image/png")
            self.end_headers()
            self.wfile.write(qrData)  # type: ignore
        else:
            self.send_response(404)


def show(qr_link: str):
    """..."""
    global webServer, qrData
    qr_img = qrcode.make(qr_link)
    qr_img.get_image()
    qr_img_path = tempfile.mktemp()
    qr_img.save(qr_img_path)
    qrData = open(qr_img_path, 'rb').read()
    os.remove(qr_img_path)
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f'请使用浏览器访问 http://<YOUR_IP>:{serverPort} 扫描二维码')
    webServer.serve_forever()


if __name__ == "__main__":
    hostName = '0.0.0.0'
    serverPort = 8080
    webServer = None
    qrData = None

    ali = Aligo(name='xxx', show=show)
    if webServer:
        webServer.server_close()  # type: ignore

    ll = ali.get_file_list()
    for f in ll:
        print(f.name, f.type, f.file_id)
