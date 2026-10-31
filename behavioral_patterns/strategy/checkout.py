from .pyment_method_type import PaymentMethodType

class Checkout:
    def proccess_payment(self, price: float, payment_method: PaymentMethodType) -> None:
        if payment_method == PaymentMethodType.VISA_CARD:
            print("processing payment of visa card")
            print("Calculate fees of the amount for visa card")

        elif payment_method == PaymentMethodType.PAYPAL:
            print("processing payment of Paypal")
            print("Calculate fees of the amount for Paypal")

        elif payment_method == PaymentMethodType.BANK_TRANSFER:
            print("processing payment of Bank Transfer")
            print("Calculate fees of the amount for Bank Transfer")