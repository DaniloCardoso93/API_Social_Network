from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from users.models import User
from .models import Follower, Friendship
from .serializers import FollowerSerializer, FriendshipSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
import ipdb


class FriendshipView(CreateAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
    lookup_url_kwarg = "user_id"

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        return super().perform_create(serializer)


class FollowerView(CreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    lookup_url_kwarg = "user_id"

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        user:User = get_object_or_404(User, id =self.kwargs[self.lookup_url_kwarg])
        # ipdb.set_trace()
        follower_obj = Follower.objects.create(followed=True)
        follower_obj.users.add(self.request.user)
        # user.followers.add(follower_obj)
        
        

