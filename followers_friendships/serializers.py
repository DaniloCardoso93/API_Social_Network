from rest_framework import serializers
from .models import Follower_Friendship

class Follower_FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower_Friendship
        fields = [
            "id",
            "followed",
            "friendship",
            "users", 
        ]
        read_only_fields = ["users"]