from rest_framework import permissions
from .models import User
from rest_framework.views import View


class CanRetrieveUserOrReadPublicPostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        ...