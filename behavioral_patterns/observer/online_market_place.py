from dataclasses import dataclass, field
from user import User
from product import Product
from offer import Offer


@dataclass
class OnlineMarketPlace:
    users: list[User] = field(default_factory=list)
    products: list[Product] = field(default_factory=list)
    offers: list[Offer] = field(default_factory=list)

    def add_user(self, user: User):
        self.users.append(user)
    
    def add_new_product(self, product: Product):
        self.products.append(product)
        self.notify_product(product=product)
    
    def add_new_offer(self, offer: Offer):
        self.offers.append(offer)
        self.notify_offer(offer=offer)
    
    def notify_product(self, product: Product):
        for user in self.users:
            if not user.is_subscribed_to_product:
                continue
            user.notify_to_product(product=product)
    
    def notify_offer(self, offer: Offer):
        for user in self.users:
            if not user._is_subscribed_to_offers:
                continue
            user.notify_to_offer(offer=offer)