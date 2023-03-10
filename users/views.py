from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import CanRetrieveUserOrReadPublicPostPermission
from drf_spectacular.utils import extend_schema

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        responses={200: UserSerializer},
        description="Rota para listagem de contas",
        summary="Listagem de Usuários",
        tags=["Tag Usuários"],
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        responses={201: UserSerializer},
        description="Rota para listagem de contas",
        summary="Criação de Usuários",
        tags=["Tag Usuários"],
    )
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CanRetrieveUserOrReadPublicPostPermission]

    lookup_url_kwarg = "user_id"

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        responses={200: UserSerializer},
        description="Rota para listagem de contas",
        summary="Listagem de Usuários",
        tags=["Tag Usuários"],
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        responses={200: UserSerializer},
        description="Rota para listagem de contas",
        summary="Alteração de Usuários",
        tags=["Tag Usuários"],
    )
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    @extend_schema(
        responses={200: UserSerializer},
        description="Rota para listagem de contas",
        summary="Alteração de Usuários",
        tags=["Tag Usuários"],
    )
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        responses={204: UserSerializer},
        description="Rota para listagem de contas",
        summary="Deleção de Usuários",
        tags=["Tag Usuários"],
    )

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)