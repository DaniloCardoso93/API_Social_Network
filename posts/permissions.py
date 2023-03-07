from rest_framework import permissions
from .models import Post
from rest_framework.views import View

class PostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Post) -> bool:
        if request.post.private:
            for user in request.user.followers_friendships:
                if user['id'] == request.post.user_id:
                    return True
        
            