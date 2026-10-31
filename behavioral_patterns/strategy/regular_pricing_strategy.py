from .pricing_strategy import IPricingStrategy


class RegularPricingStrategy(IPricingStrategy):
    def calculate_price(self, price: float) -> float:
            return price