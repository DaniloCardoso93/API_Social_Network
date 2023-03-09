from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField()
    class Meta:
        model = Like
        fields = [
            "id",
            "liked",
            "post",
        ]

        read_only_fields = ["post"]

    def get_post(self, obj: Like):
        res = {
            "username": obj.post.user.username,
            "description":obj.post.description         
        }
        return res
