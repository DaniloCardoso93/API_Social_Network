from django.db import models


class InvitationChoices(models.TextChoices):
    DEFAULT = "Send"
    ACCEPTED = "Accepted"
    REFUSED = "Refused"


class Friendship(models.Model):
    class Meta:
        ordering = ("id",)

    sending_user = models.ForeignKey("users.User", related_name="sending_friend", on_delete=models.CASCADE,)
    receiving_user = models.ForeignKey("users.User", related_name="receiving_friend", on_delete=models.CASCADE,)
    invitation = models.CharField(max_length=20, choices=InvitationChoices.choices, default=InvitationChoices.DEFAULT)



    # tenho dado de quem enviou e quem recebeu, ja fazendo relaçao com a tabela de usuario
    # se o pending estiver falso o usuario_recebeu
