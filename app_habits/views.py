from rest_framework import generics

from app_habits.models import Habit
from app_habits.paginators import HabitPaginator
from app_habits.serializers import HabitSerializer
from app_user.models import User


class HabitCreateAPIView(generics.CreateAPIView):
    """API class for habit creation"""

    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        if isinstance(self.request.user, User):
            serializer.save(owner=self.request.user)
        serializer.save()


class HabitListAPIView(generics.ListAPIView):
    """API class shows list of habits"""

    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    queryset = Habit.objects.all()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
