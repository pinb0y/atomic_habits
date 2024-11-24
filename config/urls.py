from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("habits/", include("app_habits.urls", namespace="Привычки")),
    path("users/", include("app_user.urls", namespace="Пользователи")),
]
