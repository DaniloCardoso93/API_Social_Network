from django.db import models


class Like(models.Model):
    class Meta:
        ordering = ["id"]

    liked = models.BooleanField(default=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="likes",
    )

    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        related_name="likes",
    )
