from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField()
    liked_at = serializers.SerializerMethodField()

    class Meta:
        model = Like
        fields = ["id", "liked", "post", "liked_at"]

        read_only_fields = ["post", "liked_at"]

    def get_post(self, obj: Like):
        res = {"username": obj.post.user.username, "description": obj.post.description}
        return res

    def get_liked_at(self, obj: Like):
        STR_FORMAT = "%d/%m/%y, %H:%M:%S"
        return obj.liked_at.strftime(STR_FORMAT)
