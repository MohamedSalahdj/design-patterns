from .pricing_strategy import IPricingStrategy


class GoldPricingStrategy(IPricingStrategy):
    def calculate_price(self, price: float) -> float:
            return price * 0.9