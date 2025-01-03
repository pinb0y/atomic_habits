from rest_framework import serializers

from app_habits.models import Habit
from app_habits.validators import (
    validate_reward_or_pleasant_habit,
    validate_linked_habit,
    validate_pleasant_habit,
)


class HabitListSerializer(serializers.ModelSerializer):
    """Сериалайзер для списка привычек"""

    # Поле условия в понятном виде.
    condition = serializers.SerializerMethodField(read_only=True)
    # Поле для отображения или награды или связанной приятной привычки
    reward_or_linked_habit = serializers.SerializerMethodField(read_only=True)

    def get_condition(self, obj):
        return f"Я буду {obj.action} {obj.time} {obj.place}"

    def get_reward_or_linked_habit(self, obj):
        if obj.linked_habit:
            return f"linked_habit '{obj.linked_habit.id}'"
        elif obj.reward:
            return f"reward '{obj.reward}'"

    class Meta:
        model = Habit
        fields = (
            "id",
            "user",
            "condition",
            "periodicity",
            "reward_or_linked_habit",
            "lead_time",
            "is_pleasant",
            "is_public",
        )


class HabitSerializer(serializers.ModelSerializer):
    """Сериалайзер для детальной привычки со всеми полями"""

    class Meta:
        model = Habit
        exclude = ("created_at", "updated_at")
        validators = [
            validate_reward_or_pleasant_habit,
            validate_linked_habit,
            validate_pleasant_habit,
        ]
