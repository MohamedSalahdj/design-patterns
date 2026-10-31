from dataclasses import dataclass

from .membership_type import MembershipType

@dataclass
class Product:
    _name: str
    _price: float

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

    def calculate_price(self, membership_type: MembershipType) -> float:
        if membership_type == MembershipType.REGULAR:
            return self.price
        elif membership_type == MembershipType.GOLD:
            return self.price * 0.9
        elif membership_type == MembershipType.PREMIUM:
            return self.price * 0.8