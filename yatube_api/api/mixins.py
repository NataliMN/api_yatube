from rest_framework.exceptions import PermissionDenied


class AuthValidationMixin:
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            if serializer.is_valid():
                serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if self.request.user.is_authenticated:
            if serializer.instance.author != self.request.user:
                raise PermissionDenied('Изменение чужого контента запрещено!')
            if serializer.is_valid():
                serializer.save()

    def perform_destroy(self, serializer):
        if serializer.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        serializer.delete()
