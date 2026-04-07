from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, user_name):
        self.user_name = user_name

    @abstractmethod
    def pay(self, amount):
        pass

    def generate_receipt(self, original, final):
        print("\n--- Payment Receipt ---")
        print(f"User: {self.user_name}")
        print(f"Original Amount: ₹{original}")
        print(f"Final Amount Paid: ₹{final}")
        print("------------------------")



class CreditCardPayment(Payment):
    def pay(self, amount):
        gateway_fee = 0.02 * amount
        gst = 0.18 * gateway_fee
        final_amount = amount + gateway_fee + gst

        self.generate_receipt(amount, final_amount)



class UPIPayment(Payment):
    def pay(self, amount):
        cashback = 50 if amount > 1000 else 0
        final_amount = amount - cashback

        self.generate_receipt(amount, final_amount)



class PayPalPayment(Payment):
    def pay(self, amount):
        transaction_fee = 0.03 * amount
        conversion_fee = 20
        final_amount = amount + transaction_fee + conversion_fee

        self.generate_receipt(amount, final_amount)



class WalletPayment(Payment):
    def __init__(self, user_name, balance):
        super().__init__(user_name)
        self.balance = balance

    def pay(self, amount):
        if amount > self.balance:
            print("\nTransaction Failed: Insufficient Wallet Balance")
        else:
            self.balance -= amount
            self.generate_receipt(amount, amount)
            print(f"Remaining Wallet Balance: ₹{self.balance}")


def process_payment(payment, amount):
    payment.pay(amount)



if __name__ == "__main__":
    p1 = CreditCardPayment("Alice")
    p2 = UPIPayment("Bob")
    p3 = PayPalPayment("Charlie")
    p4 = WalletPayment("Daisy", 500)

    process_payment(p1, 1000)
    process_payment(p2, 1200)
    process_payment(p3, 2000)
    process_payment(p4, 300)
    process_payment(p4, 300)
