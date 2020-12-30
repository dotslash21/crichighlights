from demo.services.notification.notification_service import NotificationService
from demo.services.notification.telegram_notification_service import TelegramNotificationService


def get_notification_service() -> NotificationService:
    """Factory method to return an instance of NotificationService.

    Returns:
        NotificationService: Instance of NotificationService

    """

    return TelegramNotificationService()
