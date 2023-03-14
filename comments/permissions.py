from rest_framework import permissions
from rest_framework.views import View
from rest_framework.request import Request
from posts.models import Post
from followers_friendships.models import Friendship


class IsAbleToCommentPermission(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Post):
        if obj.can_comment:
            return True

        if not obj.can_comment:
            friends = Friendship.objects.filter(invitation="Accepted")
            for friend in friends:
                if (
                    friend.sending_user == obj.user
                    and request.user == friend.receiving_user
                ):
                    return True
                if (
                    friend.receiving_user == obj.user
                    and request.user == friend.sending_user
                ):
                    return True

        return False
