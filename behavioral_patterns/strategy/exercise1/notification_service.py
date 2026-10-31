from dataclasses import dataclass

from .notification_strategy import NotificationStrategy

@dataclass
class NotificationService:
    _notification_strategy: NotificationStrategy

    def send_notification(self, user, message: str) -> None:
        self._notification_strategy.send_notification(user=user, message=message)
