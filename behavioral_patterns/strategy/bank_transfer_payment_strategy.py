from .payment_strategy import IPaymentStrategy

class BankTransferPaymentStrategy(IPaymentStrategy):
    def process_payment(self, price):
        print("processing payment of Bank Transfer")
        print(f"Calculate fees of the amount {price} for Bank Transfer")
