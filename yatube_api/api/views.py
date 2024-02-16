from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .mixins import AuthValidationMixin
from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class PostViewSet(AuthValidationMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(AuthValidationMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
            serializer.save(author=self.request.user,
                            post=post)
