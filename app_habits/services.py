import requests

from config.settings import TELEGRAM_TOKEN, TELEGRAM_URL


def send_message_to_telegram(message, tg_id):
    """Отправляет сообщение в Telegram по tg_id"""
    params = {
        "text": message,
        "chat_id": tg_id,
    }
    requests.get(f"{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage", params=params)
