from rest_framework.exceptions import ValidationError


def validate_reward_or_pleasant_habit(obj):
    """Исключает одновременный выбор приятной привычки и вознаграждения."""
    reward = dict(obj).get("reward")
    linked_habit = dict(obj).get("linked_habit")
    if reward and linked_habit:
        raise ValidationError(
            "Нельзя выбирать приятную привычку и вознаграждение вместе"
        )


def validate_linked_habit(obj):
    """Проверяет, что в связанные привычки могут попадать только привычки с признаком приятная."""
    linked_habit = dict(obj).get("linked_habit")
    if linked_habit and not linked_habit.is_pleasant:
        raise ValidationError("Связанная привычка должна быть приятной")


def validate_pleasant_habit(obj):
    """Проверяет, что у приятной привычки нет вознаграждения или связанной привычки."""
    is_pleasant = dict(obj).get("is_pleasant", None)
    reward = dict(obj).get("reward", None)
    linked_habit = dict(obj).get("linked_habit", None)
    if is_pleasant and (linked_habit or reward):
        raise ValidationError(
            "Приятная привычка не может быть связана с другой приятной привычкой или вознаграждением."
        )
