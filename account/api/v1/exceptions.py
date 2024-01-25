from rest_framework.exceptions import APIException


class OldPasswordException(APIException):
    status_code = 409
    default_detail = 'Old password error'