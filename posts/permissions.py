from rest_framework import permissions
from .models import Post
from users.models import User
from rest_framework.views import View


class IsFollowerOrFriendPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Post) -> bool:
        post_owner = User.objects.get(id=obj.user_id)
        allowed_methods = ["PATCH", "DELETE"]

        if request.method in allowed_methods:
            return post_owner == request.user

        if post_owner == request.user:
            return True

        if obj.private:
            for user in list(post_owner.followers.all()):
                if user.id == request.user.id:
                    return True

            for friend in list(post_owner.receiving_friend.all()):
                if request.user.id == friend.sending_user_id:
                    return friend.invitation == "Accepted"
        else:
            return True

        return False