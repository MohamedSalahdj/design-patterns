from dataclasses import dataclass, field
from subscriber import Subscriber
from product import Product
from offer import Offer
from event_type import EventType


@dataclass
class OnlineMarketPlace:
    subscribers: dict[EventType, list[Subscriber]] = field(default_factory=dict)
    products: list[Product] = field(default_factory=list)
    offers: list[Offer] = field(default_factory=list)

    def subscribe(self, event_type: EventType, subscriber: Subscriber):
        self.subscribers.setdefault(event_type, []).append(subscriber)

    def unsubscribe(self, event_type: EventType, subscriber: Subscriber):
        self.subscribers.get(event_type).remove(subscriber)

    def add_new_product(self, product: Product):
        self.products.append(product)
        self.notify_subscriber(EventType.NEW_PRODUCT, f"New product is added: {product.name}")
    
    def add_new_offer(self, offer: Offer):
        self.offers.append(offer)
        self.notify_subscriber(EventType.NEW_OFFER, f"New offer is added: {offer.message}")
    
    def notify_subscriber(self, event_type: EventType, message: str):
        for subscriber in self.subscribers.get(event_type):
            subscriber.notify(message=message)