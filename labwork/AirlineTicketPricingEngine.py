# Airline Ticket Pricing Engine using Selection Statements

age = int(input("Enter Passenger Age: "))
business_class = input("Business Class (Y/N): ").strip().upper()
window_seat = input("Window Seat (Y/N): ").strip().upper()
weekend_travel = input("Weekend Travel (Y/N): ").strip().upper()

base_fare = 5000
additional_charges = 0

# Selection statements for charges
if business_class == "Y":
    additional_charges += 3000

if window_seat == "Y":
    additional_charges += 500

if weekend_travel == "Y":
    additional_charges += 1000

total_fare = base_fare + additional_charges

# Selection statements for discount
if age < 12:
    discount = 0.50
    discount_type = "Child Discount: 50%"
elif age > 60:
    discount = 0.20
    discount_type = "Senior Citizen Discount: 20%"
else:
    discount = 0
    discount_type = "No Discount"

final_fare = total_fare - (total_fare * discount)

# Output
print("Base Fare: ₹", base_fare)
print("Additional Charges: ₹", additional_charges)
print(discount_type)
print("Final Ticket Fare: ₹", final_fare)
