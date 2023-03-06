from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User, UserGender


def choices_error_message(choices_class):
    valid_choices = [choice[0] for choice in choices_class]
    message = ", ".join(valid_choices).rsplit(",", 1)

    return "Choose between " + " and".join(message) + "."


class UserSerializer(serializers.ModelSerializer):
    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if key == "password":
                instance.set_password(value)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "birthdate",
            "gender",
            "followers_friendships"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "followers_friendships":{"read_only": True},
            "gender": {
                "error_message": {
                    "invalid_choice": choices_error_message(UserGender),
                }
            },
        }
