from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import LikeSerializer
from rest_framework.generics import DestroyAPIView, ListCreateAPIView
from posts.models import Post
from .models import Like
from users.permissions import IsAuthenticatedAndAccountOwner
from drf_spectacular.utils import extend_schema


class LikeView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    lookup_url_kwarg = "post_id"

    @extend_schema(
        responses={200},
        description="Rota para listagem de contas",
        summary="Listagem de Curtidas",
        tags=["Tag Curtidas"],
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        responses={201},
        description="Rota para Adição de curtidas",
        summary="Adição de Curtidas",
        tags=["Tag Curtidas"],
    )
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer: LikeSerializer):
        post: Post = get_object_or_404(Post, id=self.kwargs[self.lookup_url_kwarg])
        return serializer.save(user=self.request.user, post=post)


class LikeDetailView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedAndAccountOwner]

    queryset = Like.objects.all()

    lookup_url_kwarg = "like_id"

    @extend_schema(
        responses={204},
        description="Rota para listagem de contas",
        summary="Remoção de Curtidas",
        tags=["Tag Curtidas"],
    )

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)