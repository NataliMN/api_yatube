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

    def get_post(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            post = self.get_post()
            serializer.save(author=self.request.user,
                            post=post)
