from django.urls import path
from .views import LikeDetailView

urlpatterns = [
    path("likes/<int:like_id>/", LikeDetailView.as_view()),
]
