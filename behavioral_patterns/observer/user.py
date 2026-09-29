from dataclasses import dataclass
from typing import Optional

from product import Product 
from offer import Offer

@dataclass
class User:
    _name: str
    _age: Optional[int] = None
    _is_subscribed_to_product: bool = False
    _is_subscribed_to_offers: bool = False

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age    
    
    @age.setter
    def age(self, new_age):
        self._age = new_age

    @property
    def is_subscribed_to_product(self):
        return self._is_subscribed_to_product
    
    @is_subscribed_to_product.setter
    def is_subscribed_to_product(self, new_is_subscribed_to_product):
        self._is_subscribed_to_product = new_is_subscribed_to_product

    @property
    def is_subscribed_to_offers(self):
        return self._is_subscribed_to_offers    
    
    @is_subscribed_to_offers.setter
    def is_subscribed_to_offers(self, new_is_subscribed_to_offers):
        self._is_subscribed_to_offers = new_is_subscribed_to_offers
    
    def notify_to_product(self, product: Product):
        print(f"Notifying {self.name} about new product -> {product.name}")
    
    def notify_to_offer(self, offer: Offer):
        print(f"Notifying {self.name} about new offer -> {offer.message}")