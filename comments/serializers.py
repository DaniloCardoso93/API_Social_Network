from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            "id",
            "description",
            "created_at",
            "user", 
        ]
        read_only_fields = ["created_at", "user"]

    def get_user(self, obj):
        res = {
            "user_id": obj.user.id,
            "username": obj.user.username
        }
        return res