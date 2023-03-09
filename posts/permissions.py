from rest_framework import permissions
from .models import Post
from users.models import User
from rest_framework.views import View
from django.forms.models import model_to_dict

class PostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Post) -> bool:
        post_owner = User.objects.get(id=obj.user_id)
        if obj.private:
            for user in list(post_owner.followers.all()):
                if user.id == request.user.id:
                    return True
