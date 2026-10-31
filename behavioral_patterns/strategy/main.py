from .product import Product
from .membership_type import MembershipType
from .checkout import Checkout
from .pyment_method_type import PaymentMethodType
from .gold_pricing_strategy import GoldPricingStrategy
from .regular_pricing_strategy import RegularPricingStrategy
from .premium_pricing_strategy import PremiumPricingStrategy
from .paypal_payment_strategy import PaypalPaymentStrategy
from .visa_card_payment_strategy import VisaCardPaymentStrategy
from .bank_transfer_payment_strategy import BankTransferPaymentStrategy


if __name__ == "__main__":
    pricing_strategy = {
        MembershipType.REGULAR: RegularPricingStrategy(),
        MembershipType.GOLD: GoldPricingStrategy(),
        MembershipType.PREMIUM: PremiumPricingStrategy()
    }    

    payment_strategy = {
        PaymentMethodType.VISA_CARD: VisaCardPaymentStrategy(),
        PaymentMethodType.PAYPAL: PaypalPaymentStrategy(),
        PaymentMethodType.BANK_TRANSFER: BankTransferPaymentStrategy()
    }    

    laptop = Product("Laptop", 15000, pricing_strategy.get(MembershipType.REGULAR))
    laptop_price = laptop.calculate_price()
    print(laptop_price)

    iphone_16 = Product("Iphone 16", 25000, pricing_strategy.get(MembershipType.GOLD))
    iphone_16_price = iphone_16.calculate_price()
    print(iphone_16_price)

    samsung_s26 = Product("samsung_s26", 35000, pricing_strategy.get(MembershipType.PREMIUM))
    samsung_s26_price = samsung_s26.calculate_price()
    print(samsung_s26_price)

    checkout1 = Checkout(payment_strategy.get(PaymentMethodType.BANK_TRANSFER))
    checkout1.proccess_payment(iphone_16_price)

    checkout2 = Checkout(payment_strategy.get(PaymentMethodType.VISA_CARD))
    checkout2.proccess_payment(samsung_s26_price)