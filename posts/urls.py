from django.urls import path
from .views import PostView, PostDetailView
from comments.views import CommentView, CommentDetailView
from likes.views import LikeView

urlpatterns = [
    path("posts/", PostView.as_view()),
    path("posts/<int:post_id>/", PostDetailView.as_view()),
    path("posts/<int:post_id>/comments/", CommentView.as_view()),
    path("posts/<int:post_id>/likes/", LikeView.as_view()),
]
