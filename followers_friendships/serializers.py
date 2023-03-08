from rest_framework import serializers
from .models import Friendship

class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = [
            "id",
            "friend",
            "users", 
        ]
        read_only_fields = ["users", "friend",]
