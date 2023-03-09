from rest_framework import permissions
from .models import Post
from users.models import User
from rest_framework.views import View
import ipdb


class PostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Post) -> bool:
        post_owner = User.objects.get(id=obj.user_id)
        if obj.private:
            for user in post_owner.followers:
                if user['id'] == request.user.id:
                    return True
