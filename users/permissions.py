from rest_framework import permissions
from .models import User
from comments.models import Comment
from rest_framework.views import View, Request
from ipdb import set_trace


class CanRetrieveUserOrReadPublicPostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return True


class IsAuthenticatedAndAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Comment) -> bool:
        return request.user.is_authenticated and request.user == obj.user


class IsCommentOrPostOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Comment) -> bool:
        if request.method == "PATCH":
            return request.user == obj.user
        return request.user == obj.user or obj.post.user == request.user
