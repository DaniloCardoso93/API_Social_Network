from rest_framework.exceptions import APIException
from rest_framework.views import status


class AlreadyLikedError(APIException):
    status_code = status.HTTP_409_CONFLICT
