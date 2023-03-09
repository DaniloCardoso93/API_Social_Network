from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import FriendshipDetailView

urlpatterns = [
    path("friendships/<int:friendship_id>/", FriendshipDetailView.as_view()),
]
