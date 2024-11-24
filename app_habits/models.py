from django.db import models

from app_user.models import User


class Habit(models.Model):
    PERIODS = (
        ("1", "Каждый день"),
        ("2", "Через день"),
        ("3", "Через два дня"),
        ("4", "Через три дня"),
        ("5", "Через четыре дня"),
        ("6", "Через пять дней"),
        ("7", "Раз в неделю"),
    )
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Выберите пользователя",
    )
    place = models.CharField(
        "Место", max_length=500, help_text="Введите место выполнения привычки"
    )
    time = models.CharField(
        "Время", max_length=500, help_text="Введите время выполнения привычки"
    )
    action = models.CharField(
        "Действие", max_length=500, help_text="Введите действие привычки"
    )
    is_pleasant = models.BooleanField(
        "Признак приятной привычки", help_text="укажите является ли привычка приятной"
    )
    linked_habit = models.ForeignKey(
        "self",
        verbose_name="Связанная привычка",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Укажите связанную привычку",
    )
    periodicity = models.CharField(
        "Периодичность",
        max_length=10,
        choices=PERIODS,
        help_text="Выберете периодичность",
    )
    lead_time = models.PositiveSmallIntegerField(
        "Примерное время выполнения",
        help_text="Укажите примерное время выполнения в секундах",
    )
    is_public = models.BooleanField(
        "Статус публичности", help_text="Укажите статус публичности"
    )
