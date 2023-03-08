from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.views import APIView, Request, Response, status
from users.models import User
from .models import Friendship
from .serializers import FriendshipSerializer
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


class FollowerView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def patch(self, request:Request, user_id:int) ->Response:
        user:User = get_object_or_404(User, id =user_id)

        user.followings.add(request.user)

        return Response(status=status.HTTP_204_NO_CONTENT)
    

        
        

