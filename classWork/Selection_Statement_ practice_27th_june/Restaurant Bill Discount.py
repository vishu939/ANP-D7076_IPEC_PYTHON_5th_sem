# Restaurant Bill Discount

bill = float(input("Enter total bill amount: "))

if bill < 1000:
    print("No Discount")
elif bill < 3000:
    print("10% Discount Applied")
else:
    print("20% Discount Applied")
