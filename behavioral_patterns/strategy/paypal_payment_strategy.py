from .payment_strategy import IPaymentStrategy

class PaypalPaymentStrategy(IPaymentStrategy):
    def process_payment(self, price):
        print("processing payment of Paypal")
        print(f"Calculate fees of the amount {price} for Paypal")
