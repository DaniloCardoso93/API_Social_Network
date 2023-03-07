from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from comments.models import Comment
from .serializers import LikeSerializer
from rest_framework.generics import CreateAPIView, DestroyAPIView
from posts.models import Post
from .models import Like
from users.permissions import IsAuthenticatedAndAccountOwner


class LikeView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Comment.objects.all()
    serializer_class = LikeSerializer

    lookup_url_kwarg = "post_id"

    def perform_create(self, serializer: LikeSerializer):
        post: Post = get_object_or_404(Post, id=self.kwargs[self.lookup_url_kwarg])
        return serializer.save(user=self.request.user, post=post)


class LikeDetailView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedAndAccountOwner]

    queryset = Like.objects.all()

    lookup_url_kwarg = "like_id"
