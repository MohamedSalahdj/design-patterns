from .payment_strategy import IPaymentStrategy

class VisaCardPaymentStrategy(IPaymentStrategy):
    def process_payment(self, price):
        print("processing payment of Visa Card")
        print(f"Calculate fees of the amount {price} for visa card")
