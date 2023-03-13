from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("comments/<int:comment_id>/", views.CommentDetailView.as_view()),
]
