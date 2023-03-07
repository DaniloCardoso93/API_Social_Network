from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import CanRetrieveUserOrReadPublicPostPermission


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CanRetrieveUserOrReadPublicPostPermission]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
