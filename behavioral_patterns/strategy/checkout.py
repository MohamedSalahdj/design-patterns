from dataclasses import dataclass
from .payment_strategy import IPaymentStrategy


@dataclass
class Checkout:
    payment_strategy: IPaymentStrategy

    def proccess_payment(self, price: float) -> None:
        self.payment_strategy.process_payment(price=price)
