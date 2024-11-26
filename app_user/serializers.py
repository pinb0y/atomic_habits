from rest_framework import serializers

from app_user.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    """Сериалайзер для регистрации пользователя"""

    class Meta:
        model = User
        fields = ("email", "password", "telegram_id")


class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели пользователя общий"""

    class Meta:
        model = User
        fields = "__all__"
