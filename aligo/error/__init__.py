class AligoException(Exception):
    pass


class AligoStatus500(AligoException):
    pass


class AligoRefreshFailed(AligoException):
    pass
