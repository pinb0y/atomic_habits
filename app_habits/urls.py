from django.urls import path

from app_habits.apps import AppHabitsConfig
from app_habits.views import (
    HabitCreateAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
)

app_name = AppHabitsConfig.name

urlpatterns = [
    path("create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("", HabitListAPIView.as_view(), name="habit-list"),
    path("<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit-get"),
    path("update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit-update"),
    path("delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit-delete"),
]
