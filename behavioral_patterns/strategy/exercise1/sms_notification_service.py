from .notification_strategy import NotificationStrategy
from .user import User

class SMSNotificationService(NotificationStrategy):
    def send_notification(self, user: User, message: str) -> None:
        print(f"Sending message: {message} to user: {user.mobile_number}")