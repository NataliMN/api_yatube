from rest_framework.exceptions import PermissionDenied


class AuthValidationMixin:
    """
    Миксин для вьюсетов поста или комментария.

    Выполняет проверку авторства при создании,
    изменении и удалении контента.
    """

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super().perform_update(serializer)

    def perform_destroy(self, serializer):
        if serializer.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super().perform_destroy(serializer)
