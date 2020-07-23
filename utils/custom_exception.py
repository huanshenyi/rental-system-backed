__author__ = "ハリネズミ"
from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.response import Response


class DataException(Exception):
    def __init__(self, code=0, status=status.HTTP_400_BAD_REQUEST, data=None, message=""):
        self.code = code
        self.status = status
        self.message = message
        self.data = data

    def __str__(self):
        return self.message


def custom_exception_handler(exc, context):

    if isinstance(exc, DataException):
        return Response(
            data={"code": exc.code, "data": exc.data, "message": exc.message},
            status=exc.status
        )

    response = exception_handler(exc, context)
    return response
