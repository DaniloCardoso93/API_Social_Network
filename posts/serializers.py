from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "description",
            "created_at",
            "private",
            "can_comment",
            "user",
            "likes",
            "comments",
        ]

        read_only_fields = ["user", "created_at", "likes", "comments"]

    def get_likes(self, obj):
        return obj.likes.count()
    
    def get_user(self, obj):
        res = {
            "user_id": obj.user.id,
            "username": obj.user.username
        }
        return res
    
    def get_comments(self, obj: Post):
        return [{"user_name": comment.user.username, "description": comment.description}
                 for comment in obj.comments.all()]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance: Post, validated_data: dict) -> Post:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
