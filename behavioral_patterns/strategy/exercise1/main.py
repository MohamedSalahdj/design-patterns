from .user import User
from .email_notification_service import EmailNotificationService
from .sms_notification_service import SMSNotificationService
from .notification_service import NotificationService

if __name__ == "__main__":
    salah = User("Salah", "salah@backend.com", "+20123456789")

    notification = NotificationService(EmailNotificationService())
    notification.send_notification(salah, "Hello")

    notification = NotificationService(SMSNotificationService())
    notification.send_notification(salah, "Hello")