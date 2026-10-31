from abc import ABC, abstractmethod

class IPaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, price: float) -> None:
        ...
