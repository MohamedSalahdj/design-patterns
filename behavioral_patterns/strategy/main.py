from .product import Product
from .membership_type import MembershipType
from .checkout import Checkout
from .pyment_method_type import PaymentMethodType


if __name__ == "__main__":
    laptop = Product("Laptop", 15000)
    laptop_price = Product.calculate_price(laptop, MembershipType.REGULAR)
    print(f"{laptop_price}")

    iphone_16 = Product("Iphone 16", 25000)
    iphone_16_price = Product.calculate_price(iphone_16, MembershipType.GOLD)
    print(iphone_16_price)

    samsung_s26 = Product("samsung_s26", 35000)
    samsung_s26_price = Product.calculate_price(samsung_s26, MembershipType.PREMIUM)
    print(samsung_s26_price)

    checkout = Checkout()
    checkout.proccess_payment(samsung_s26_price, PaymentMethodType.BANK_TRANSFER)