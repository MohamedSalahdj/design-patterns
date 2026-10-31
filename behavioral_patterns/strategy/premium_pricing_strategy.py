from .pricing_strategy import IPricingStrategy


class PremiumPricingStrategy(IPricingStrategy):
    def calculate_price(self, price: float) -> float:
            return price * 0.8