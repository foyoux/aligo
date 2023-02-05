"""..."""
import requests


class Null:
    """表示一个失败的结果"""

    def __init__(self, response: requests.Response):
        self.response = response
        # noinspection PyBroadException
        try:
            d = response.json()
        except Exception:
            pass
        else:
            self.code = d.get('code')
            self.message = d.get('message')
            self.requestId = d.get('requestId')
            self.resultCode = d.get('resultCode')

    def __repr__(self):
        return self.response.text

    def __bool__(self):
        return False
