from posts.models import Comment, Group, Post
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    """Cериализатор для комментариев."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('created', 'post')


class GroupSerializer(serializers.ModelSerializer):
    """Cериализатор для групп постов."""

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Cериализатор для публикауций."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        read_only = ('pub_date')
