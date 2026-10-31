from abc import ABC, abstractmethod


class IPricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, price: float) -> float:
        ...