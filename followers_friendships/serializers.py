from rest_framework import serializers
from .models import Follower, Friendship

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = [
            "id",
            "followed",
            "users", 
        ]
        read_only_fields = ["users", "followed",]


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = [
            "id",
            "friend",
            "users", 
        ]
        read_only_fields = ["users", "friend",]
