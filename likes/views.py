from django.shortcuts import render
from rest_framework.generics import  CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
