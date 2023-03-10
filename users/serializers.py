from rest_framework import serializers
from .models import User, UserGender
from utils.utils import choices_error_message
from followers_friendships.models import Friendship
import ipdb
from django.forms.models import model_to_dict

class UserSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    friends = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "birthdate",
            "gender",
            "followers",
            "friends"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "followers": {"read_only": True},
            "friends": {"read_only": True},
            "gender": {
                "error_messages": {"invalid_choice": choices_error_message(UserGender)}
            },
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if key == "password":
                instance.set_password(value)
        instance.save()

        return instance

    def get_followers(self, obj: User):
        return [
            {"follower_id": follower.id, "follower_username": follower.username}
            for follower in obj.followers.all()
        ]

    def get_friends(self, obj: User):
        friends = Friendship.objects.filter(invitation="Accepted")
        list = []

        for friend in friends:
            if friend.sending_user == obj:
               list.append({"friend_id":friend.receiving_user.id, "friend_user": friend.receiving_user.username})
            if friend.receiving_user == obj:
                list.append({"friend_id": friend.sending_user.id, "friend_user": friend.sending_user.username})

        return list

        