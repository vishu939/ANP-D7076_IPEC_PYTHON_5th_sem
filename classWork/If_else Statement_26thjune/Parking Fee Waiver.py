# Parking Fee Waiver

purchase = float(input("Enter the purchase amount: "))

if purchase >= 2000:
    fee = 0
    print("Parking Fee Waived!")
else:
    fee = 100
    print("Parking Fee Applicable!")

print("Parking Fee: ₹", fee)
