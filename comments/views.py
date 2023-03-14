from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from comments.models import Comment
from comments.permissions import IsAbleToCommentPermission
from .serializers import CommentSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from posts.models import Post
from users.permissions import IsCommentOrPostOwner
from drf_spectacular.utils import extend_schema


class CommentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAbleToCommentPermission, IsAuthenticated]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    lookup_url_kwarg = "post_id"

    @extend_schema(
        responses={201: CommentSerializer},
        description="Rota para criação de comentários",
        summary="Criação de Comentários",
        tags=["Tag Comentários"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer: CommentSerializer):
        post: Post = get_object_or_404(Post, id=self.kwargs[self.lookup_url_kwarg])
        self.check_object_permissions(self.request, post)
        return serializer.save(user=self.request.user, post=post)


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCommentOrPostOwner]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    lookup_url_kwarg = "comment_id"

    @extend_schema(
        responses={200: CommentSerializer},
        description="Rota para listagem de Comentários",
        summary="Listagem de Comentários",
        tags=["Tag Comentários"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        responses={200: CommentSerializer},
        description="Rota para listagem de Comentários",
        summary="Alteração de Comentários",
        tags=["Tag Comentários"],
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        responses={200: CommentSerializer},
        description="Rota para listagem de Comentários",
        summary="Alteração de Comentários",
        tags=["Tag Comentários"],
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        responses={204: CommentSerializer},
        description="Rota para listagem de Comentários",
        summary="Deleção de Comentários",
        tags=["Tag Comentários"],
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
