# define Python user-defined exceptions
class MalformedRequestError(Exception):
    "the request is malformed, i.e. missing content"
    pass

class DeviceNotFoundError(Exception):
    "a device couldn't be found"
    pass
    
class UserNotFoundError(Exception):
    "user couldn't be found (incorrect username/password)"
    pass
    
class IncorrectCredentialsError(Exception):
    "credentials are incorrect"
    pass

class UnauthorizedError(Exception):
    "package name or api key is incorrect"
    pass
    
class PayloadTooLargeError(Exception):
    "your image is too big (> 5 MB)"
    pass
    
class UnsupportedMediaTypeError(Exception):
    "you passed an invalid file type or the device(s) you tried to send this image to can\'t receive images)"
    pass
    
class UnknownError(Exception):
    "an unknown error occured! please contact the author of this module!"
    pass