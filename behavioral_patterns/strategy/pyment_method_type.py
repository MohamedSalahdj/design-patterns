from enum import Enum


class PaymentMethodType(Enum):
    VISA_CARD = "visa_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"
