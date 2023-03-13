from django.db import models


class Post(models.Model):
    class Meta:
        ordering = ("id",)

    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)
    can_comment = models.BooleanField(default=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts"
    )
