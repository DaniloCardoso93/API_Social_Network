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
            "user_id",
            "like",
            "comment",
        ]

        read_only_fields = ["user_id", "created_at"]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance: Post, validated_data: dict) -> Post:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()  
        return instance