from rest_framework import permissions
from .models import Post
from users.models import User
from rest_framework.views import View
from utils.utils import check_follows_or_friends


class IsFollowerOrFriendPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Post) -> bool:

        post_owner = User.objects.get(id=obj.user_id)

        allowed_methods = ["PATCH", "DELETE"]

        if request.method in allowed_methods or post_owner == request.user:
            return post_owner == request.user

        if obj.private:
            private = check_follows_or_friends(request, post_owner)
            return private
        else:
            return True