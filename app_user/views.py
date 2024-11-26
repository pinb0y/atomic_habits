from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_jwt.permissions import IsSuperUser

from app_user.models import User
from app_user.permissions import IsOwner
from app_user.serializers import UserSerializer, UserRegisterSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Класс для создания пользователя"""

    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """Класс для отображения списка пользователей"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsSuperUser,)


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Класс для отображения одного пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (
        IsSuperUser,
        IsOwner,
    )


class UserUpdateAPIView(generics.UpdateAPIView):
    """Класс для редактирования пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (
        IsSuperUser,
        IsOwner,
    )


class UserDestroyAPIView(generics.DestroyAPIView):
    """Класс для удаления пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (
        IsSuperUser,
        IsOwner,
    )
