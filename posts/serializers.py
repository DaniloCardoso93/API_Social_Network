from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "description", 
            "created_at", 
            "private", 
            "can_comment", 
            "user", 
            "like", 
            "comment",
        ]

        read_only_fields = ["user", "created_at"]