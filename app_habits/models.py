from django.core.validators import MaxValueValidator
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
        "Признак приятной привычки",
        default=False,
        help_text="укажите является ли привычка приятной"
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
    reward = models.CharField(
        "Вознаграждение",
        max_length=500,
        null=True,
        blank=True,
        help_text="Укажите вознаграждение",
    )
    lead_time = models.PositiveSmallIntegerField(
        "Примерное время выполнения",
        validators=[MaxValueValidator(120)],
        help_text="Укажите примерное время выполнения в секундах",
    )
    is_public = models.BooleanField(
        "Статус публичности",
        default=False,
        help_text="Укажите статус публичности"
    )
    created_at = models.DateTimeField("Дата и время создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата и время обновления", auto_now=True)

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ("created_at",)

    def __str__(self):
        return f"Я буду {self.action} {self.time} {self.place}"
