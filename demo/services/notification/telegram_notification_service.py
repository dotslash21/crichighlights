import requests

from demo import secrets
from demo.services.notification.notification_service import NotificationService


class TelegramNotificationService(NotificationService):
    def __init__(self):
        pass

    def send(self, message: str) -> None:
        url = 'https://api.telegram.org/bot' + secrets.BOT_KEY + '/sendMessage'

        try:
            requests.post(url, data={"chat_id": secrets.CHAT_ID, "text": message})
        except Exception as e:
            raise e
