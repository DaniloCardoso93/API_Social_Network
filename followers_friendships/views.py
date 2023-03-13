from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView, Request, Response, status
from .permissions import IsReceivingFriendshipUser
from users.models import User
from .models import Friendship
from .serializers import FriendshipSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema


class FriendshipView(CreateAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
    lookup_url_kwarg = "user_id"

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={201: FriendshipSerializer},
        description="Rota para pedido de amizade",
        summary="Pedido de Amizade",
        tags=["Tag Amigos"],
    )
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        user: User = get_object_or_404(User, id=self.kwargs[self.lookup_url_kwarg])

        invitantion_obj = serializer.save(
            sending_user=self.request.user, receiving_user=user
        )

        return invitantion_obj


class FriendshipDetailView(UpdateAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
    lookup_url_kwarg = "friendship_id"

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsReceivingFriendshipUser]

    @extend_schema(
        responses={200: FriendshipSerializer},
        description="Rota para remoção de amizade",
        summary="Remoção de Amizade",
        tags=["Tag Amigos"],
    )
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    @extend_schema(
        responses={200: FriendshipSerializer},
        description="Rota para remoção de amizade",
        summary="Remoção de Amizade",
        tags=["Tag Amigos"],
    )
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class FollowerView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request: Request, user_id: int) -> Response:
        user: User = get_object_or_404(User, id=user_id)

        user.followers.add(request.user)

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @extend_schema(
        responses={204},
        description="Rota parar de Seguir",
        summary="Parar de Seguir",
        tags=["Tag Seguidores"],
    )
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    @extend_schema(
        responses={204},
        description="Rota para listagem de seguidores",
        summary="Parar de Seguir",
        tags=["Tag Seguidores"],
    )
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
