from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsFollowerOrFriendPermission
from .models import Post
from .serializers import PostSerializer
from drf_spectacular.utils import extend_schema
from django.contrib.auth.models import AnonymousUser
from utils.utils import check_follows_or_friends
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @extend_schema(
        responses={200: PostSerializer},
        description="Rota para listagem de postagens",
        summary="Listagem de Postagens",
        tags=["Tag Postagens"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        responses={201: PostSerializer},
        description="Rota para listagem de postagens",
        summary="Criação de Postagens",
        tags=["Tag Postagens"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):

        if isinstance(self.request.user, AnonymousUser):
            return Post.objects.filter(private=False)
        posts = Post.objects.all()
        return [post for post in posts if check_follows_or_friends(self.request, post.user) or post.private is False]


class PostDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsFollowerOrFriendPermission]

    lookup_url_kwarg = "post_id"

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @extend_schema(
        responses={200: PostSerializer},
        description="Rota para listagem de postagens",
        summary="Listagem de Postagens",
        tags=["Tag Postagens"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        responses={200: PostSerializer},
        description="Rota para listagem de postagens",
        summary="Alteração de Postagens",
        tags=["Tag Postagens"],
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        responses={200: PostSerializer},
        description="Rota para listagem de postagens",
        summary="Alteração de Postagens",
        tags=["Tag Postagens"],
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        responses={204: PostSerializer},
        description="Rota para listagem de postagens",
        summary="Deleção de Postagens",
        tags=["Tag Postagens"],
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
