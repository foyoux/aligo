"""扫描二维码登录服务，供登录使用"""
from http.server import BaseHTTPRequestHandler
from typing import Any


class LoginServer(BaseHTTPRequestHandler):
    """..."""

    # noinspection PyPep8Naming
    def do_GET(self):
        """..."""
        if self.path == '/':
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
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
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.end_headers()
            # noinspection PyUnresolvedReferences
            self.wfile.write(self.server.qrData)
        elif self.path == '/close':
            self.server.server_close()
        else:
            self.send_response(404)

    def log_message(self, _format: str, *args: Any) -> None:
        """..."""
        return
