class BadRequestError(Exception):
    def __init__(self, message=None, *args, **kwargs):
        super(BadRequestError, self).__init__(message)


class AmountMismatchError(Exception):
    def __init__(self, message=None, *args, **kwargs):
        super(AmountMismatchError, self).__init__(message)


class ServerError(Exception):
    def __init__(self, message=None, *args, **kwargs):
        super(ServerError, self).__init__(message)


class AuthError(Exception):
    def __init__(self, message=None, *args, **kwargs):
        super(AuthError, self).__init__(message)
