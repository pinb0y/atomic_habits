from django.urls import path

from app_user.apps import AppUserConfig
from app_user.views import UserCreateAPIView

app_name = AppUserConfig.name

urlpatterns = [path("create/", UserCreateAPIView.as_view(), name="user-create")]
