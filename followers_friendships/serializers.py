from rest_framework import serializers
from .models import Friendship, InvitationChoices
from utils.utils import choices_error_message


class FriendshipSerializer(serializers.ModelSerializer):
    receiving_user = serializers.SerializerMethodField()
    sending_user = serializers.SerializerMethodField()

    class Meta:
        model = Friendship
        fields = [
            "id",
            "sending_user",
            "receiving_user",
            "invitation",
        ]
        read_only_fields = [
            "sending_user",
            "receiving_user",
        ]

        extra_kwargs = {
            "invitation": {
                "error_messages": {
                    "invalid_choice": choices_error_message(InvitationChoices)
                }
            }
        }

    def get_receiving_user(self, obj):
        res = {
            "receiving_user_id": obj.receiving_user.id,
            "receiving_username": obj.receiving_user.username,
        }
        return res

    def get_sending_user(self, obj):
        res = {
            "sending_user_id": obj.sending_user.id,
            "sending_username": obj.sending_user.username,
        }
        return res
