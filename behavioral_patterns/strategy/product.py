from dataclasses import dataclass

from .pricing_strategy import IPricingStrategy


@dataclass
class Product:
    _name: str
    _price: float
    _pricing_startegy: IPricingStrategy

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        self._price = new_price

    @property
    def pricing_startegy(self) -> IPricingStrategy:
        return self._pricing_startegy
    
    @pricing_startegy.setter
    def pricing_startegy(self, new_pricing_startegy: IPricingStrategy) -> None:
        self._pricing_startegy = new_pricing_startegy
    

    def calculate_price(self) -> float:
        return self._pricing_startegy.calculate_price(price=self.price)