# Electricity Bill Discount

bill = float(input("Enter the electricity bill amount: "))

if bill >= 5000:
    discount = bill * 0.10
    final_amount = bill - discount
    print("Discount Applied!")
else:
    discount = 0
    final_amount = bill
    print("No Discount Applied!")

print("Final Bill Amount: ₹", final_amount)
