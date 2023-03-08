from django.db import models


class Follower(models.Model):
    class Meta:
        ordering = ("id",)

    followed = models.BooleanField(default=False)
    following = models.ForeignKey("users.User", related_name="followers", on_delete=models.CASCADE,)
    # users = models.ManyToManyField(
    #     "users.User",
    #     related_name="followers",
    # )


class Friendship(models.Model):
    class Meta:
        ordering = ("id",)

    friend = models.BooleanField(default=False)
    users = models.ManyToManyField(
        "users.User",
        related_name="friendships",
    )