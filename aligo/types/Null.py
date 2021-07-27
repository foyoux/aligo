"""..."""
import requests


class Null:
    """表示一个失败的结果"""

    def __init__(self, response: requests.Response):
        self.response = response

    def __repr__(self):
        return self.response.text

    def __bool__(self):
        return False
