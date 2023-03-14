from rest_framework import permissions
from .models import User
from rest_framework.views import View, Request
from likes.models import Like


class IsAccountOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        if request.method == "GET":
            return True
        return request.user.is_authenticated and request.user == obj


class IsLikeOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Like) -> bool:
        if request.method == "GET":
            return True
        return request.user.is_authenticated and request.user == obj.user


class IsCommentOrPostOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        if request.method == "PATCH":
            return request.user == obj.user
        return request.user == obj.user or obj.post.user == request.user
