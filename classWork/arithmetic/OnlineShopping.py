# Program to calculate final payable amount after discount

# Input values
fixed_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate discount amount
discount_amount = (fixed_price * discount_percent) / 100

# Final payable amount
final_amount = fixed_price - discount_amount

# Output
print("Discount Amount:", discount_amount)
print("Final Payable Amount:", final_amount)
