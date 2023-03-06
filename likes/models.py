from django.db import models


class Like(models.Model):
    class Meta:
        ordering = ["id"]

    liked = models.BooleanField(default=False)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="likes",
    )
