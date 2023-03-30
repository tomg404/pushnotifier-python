class MalformedRequestError(Exception):
    def __init__(self, message="the request is malformed, i.e. missing content"):
        super().__init__(message)


class DeviceNotFoundError(Exception):
    def __init__(self, message="a device couldn't be found"):
        super().__init__(message)


class UserNotFoundError(Exception):
    def __init__(self, message="user couldn't be found (incorrect username/password)"):
        super().__init__(message)


class IncorrectCredentialsError(Exception):
    def __init__(self, message="credentials are incorrect"):
        super().__init__(message)


class UnauthorizedError(Exception):
    def __int__(self, message="package name or api key is incorrect"):
        super().__init__(message)


class PayloadTooLargeError(Exception):
    def __init__(self, message="your image is too big (> 5 MB)"):
        super().__init__(message)


class UnsupportedMediaTypeError(Exception):
    def __init__(
        self,
        message="you passed an invalid file type or the device(s) you tried to send this image to can't receive images",
    ):
        super().__init__(message)


class UnknownError(Exception):
    def __init__(
        self,
        message="an unknown error occurred! please contact the author of this module!",
    ):
        super().__init__(message)
