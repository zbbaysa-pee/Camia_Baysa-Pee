payment = str(input("Enter payment method (Cash, GCash, Card): ")).lower()
valid_payments = ["cash", "gcash", "card"]

if payment in valid_payments:
    print("Valid payment method.")
else:
    print("Invalid payment method.")
