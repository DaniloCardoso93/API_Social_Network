from rest_framework import permissions
from .models import Friendship
from rest_framework.views import View, Request


class IsReceivingFriendshipUser(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, obj: Friendship
    ) -> bool:
        return request.user.is_authenticated and request.user == obj.receiving_user
