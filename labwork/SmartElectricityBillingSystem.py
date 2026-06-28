# Smart Electricity Billing System

units = int(input("Enter Units Consumed: "))
consumer_type = input("Consumer Type (Residential/Commercial): ")
senior = input("Senior Citizen (Y/N): ")

# Step 1: Base Bill Calculation
if units <= 100:
    base_bill = units * 5
elif units <= 300:
    base_bill = (100 * 5) + (units - 100) * 7
else:
    base_bill = (100 * 5) + (200 * 7) + (units - 300) * 10

# Step 2: Commercial Charge
commercial_charge = 0
if consumer_type.lower() == "commercial":
    commercial_charge = base_bill * 0.20

# Step 3: Surcharge
surcharge = 0
if base_bill + commercial_charge > 5000:
    surcharge = (base_bill + commercial_charge) * 0.05

# Step 4: Senior Citizen Discount
discount = 0
if senior.upper() == "Y":
    discount = (base_bill + commercial_charge + surcharge) * 0.10

# Final Bill
final_bill = base_bill + commercial_charge + surcharge - discount

# Output
print("Base Bill: ₹", base_bill)
print("Commercial Charge: ₹", commercial_charge)
print("Surcharge: ₹", surcharge)
print("Senior Citizen Discount: ₹", discount)
print("Final Bill Amount: ₹", final_bill)
