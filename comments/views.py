from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from comments.models import Comment
from .serializers import CommentSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from posts.models import Post
from ipdb import set_trace
from users.permissions import IsCommentOrPostOwner


class CommentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    lookup_url_kwarg = "post_id"

    def perform_create(self, serializer: CommentSerializer):
        post: Post = get_object_or_404(Post, id=self.kwargs[self.lookup_url_kwarg])
        return serializer.save(user=self.request.user, post=post)


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCommentOrPostOwner]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    lookup_url_kwarg = "comment_id"
