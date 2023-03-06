from django.db import models


class Follower_Friendship(models.Model):
    class Meta:
        ordering = ("id",)

    followed = models.BooleanField(default=False)
    friendship = models.BooleanField(default=False)
    users = models.ManyToManyField(
        "users.User",
        related_name="followers_friendships",
    )
