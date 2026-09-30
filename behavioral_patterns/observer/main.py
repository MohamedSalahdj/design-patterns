from customer import Customer
from product import Product
from offer import Offer
from online_market_place import OnlineMarketPlace
from event_type import EventType

if __name__ == "__main__":
    online_market_place = OnlineMarketPlace()
    
    salah = Customer("Salah", 27)
    saad = Customer("Saad", 30)
    mark = Customer("Mark", 22)
    ziad = Customer("Ziad", 26)

    online_market_place.subscribe(EventType.NEW_PRODUCT, salah)
    online_market_place.subscribe(EventType.NEW_OFFER, salah)
    online_market_place.subscribe(EventType.NEW_OFFER, saad)
    online_market_place.subscribe(EventType.NEW_PRODUCT, ziad)

    online_market_place.add_new_product(Product("iphone-8", 199, 5))
    online_market_place.add_new_offer(Offer("New Offer with 23%% for every item"))