from user import User
from product import Product
from offer import Offer
from online_market_place import OnlineMarketPlace


if __name__ == "__main__":
    online_market_place = OnlineMarketPlace()
    
    online_market_place.add_user(User("Salah", 27, True, True))
    online_market_place.add_user(User("Saad", 30, True, False))
    online_market_place.add_user(User("Mark", 22, False, True))
    online_market_place.add_user(User("Ziad", 26, False, False))

    online_market_place.add_new_product(Product("iphone-8", 199, 5))
    online_market_place.add_new_offer(Offer("New Offer with 23%% for every item"))