from django.db import models


class Comment(models.Model):
    class Meta:
        ordering = ("id",)

    description = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comments",
    )
