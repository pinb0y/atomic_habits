from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app_habits.models import Habit
from app_habits.paginators import HabitPaginator
from app_habits.serializers import HabitSerializer, HabitListSerializer
from app_user.models import User
from app_user.permissions import IsOwner


class HabitCreateAPIView(generics.CreateAPIView):
    """Апи класс для создания привычки"""

    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        if isinstance(self.request.user, User):
            serializer.save(user=self.request.user)
        serializer.save()


class HabitListAPIView(generics.ListAPIView):
    """Апи класс для отображения списка привычек"""

    serializer_class = HabitListSerializer
    pagination_class = HabitPaginator
    queryset = Habit.objects.all()
    permission_classes = (
        IsOwner,
        IsAuthenticated,
    )


class HabitPublicListView(generics.ListAPIView):
    """Апи класс для отображения списка публичных привычек"""

    serializer_class = HabitListSerializer
    pagination_class = HabitPaginator
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = (IsAuthenticated,)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Апи класс для отображения одной привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner, IsAuthenticated)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Апи класс для редактирования привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner, IsAuthenticated)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Апи класс для удаления привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner, IsAuthenticated)
