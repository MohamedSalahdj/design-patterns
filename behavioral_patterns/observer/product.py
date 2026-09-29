from dataclasses import dataclass


@dataclass
class Product:
    _name : str
    _price: float
    _quantity: int

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price: float):
        self._price = new_price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: int):
        self._quantity = new_quantity
