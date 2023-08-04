import time


class LoginTimeout:
    def __init__(self, timeout: float = None):
        self.timeout = timeout
        if timeout is not None:
            assert isinstance(timeout, (int, float))
            self.start_time = time.time()

    def check_timeout(self):
        if self.timeout and self.start_time + self.timeout < time.time():
            raise TimeoutError(f'登录超时 {self.timeout}')
