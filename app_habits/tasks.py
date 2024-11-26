from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from app_habits.models import Habit
from app_habits.services import send_message_to_telegram

CURRENT_TIME = timezone.now()


@shared_task
def send_reminder_to_telegram():
    """Отправляет напоминания в Telegram-чат"""
    habits = Habit.objects.filter(user__isnull=False)
    for habit in habits:
        tg_id = habit.user.telegram_id
        message = "Привет, тебе сегодня нужно"
        message += f"\n\nСделать: {habit.action}"
        message += f"\nГде: {habit.place}"
        message += f"\nКогда: {habit.time}"
        if habit.next_send_date is None:
            send_message_to_telegram(message, tg_id)
            habit.next_send_date = CURRENT_TIME
        elif habit.next_send_date < CURRENT_TIME:
            send_message_to_telegram(message, tg_id)
            habit.next_send_date = CURRENT_TIME + timedelta(days=habit.periodicity)
        habit.save()
