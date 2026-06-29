# Courier Delivery Charge

weight = float(input("Enter package weight (kg): "))

if weight <= 2:
    print("Delivery Charge = ₹50")
elif weight <= 5:
    print("Delivery Charge = ₹100")
else:
    print("Delivery Charge = ₹180")
