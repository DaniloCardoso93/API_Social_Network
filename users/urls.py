from django.urls import path
from .views import UserView, UserDetailView
from rest_framework_simplejwt import views as jwt_views
from followers_friendships.views import FollowerView, FriendshipView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("users/<int:user_id>/friendships/", FriendshipView.as_view()),
    path("users/<int:user_id>/followers/", FollowerView.as_view()),
]
