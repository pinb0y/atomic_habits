from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app_user.apps import AppUserConfig
from app_user.views import UserCreateAPIView, UserUpdateAPIView, UserListAPIView

app_name = AppUserConfig.name

urlpatterns = [
    path("create/", UserCreateAPIView.as_view(), name="user-create"),
    path("", UserListAPIView.as_view(), name="user-list"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="user-update"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
