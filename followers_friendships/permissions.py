from rest_framework import permissions
from users.models import User
from .models import Friendship
from rest_framework.views import View, Request
from ipdb import set_trace


class CanRetrieveUserOrReadPublicPostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return True


class IsReceivingFriendshipUser(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, obj: Friendship
    ) -> bool:
        return request.user.is_authenticated and request.user == obj.receiving_user
