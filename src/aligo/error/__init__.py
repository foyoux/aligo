class AligoException(Exception):
    pass


class AligoFatalError(AligoException):
    pass


class AligoStatus500(AligoException):
    pass


class AligoRefreshFailed(AligoException):
    pass


class AligoShareLinkCreateExceedDailyLimit(AligoException):
    pass
