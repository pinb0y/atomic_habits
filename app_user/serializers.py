from rest_framework import serializers

from app_user.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "telegram_id")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

