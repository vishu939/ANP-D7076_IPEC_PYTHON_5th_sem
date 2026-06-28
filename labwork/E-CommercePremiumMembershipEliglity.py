# Premium Membership Eligibility

purchases = int(input("Enter Total Purchases: "))
orders = int(input("Enter Orders Completed: "))
rating = float(input("Enter Customer Rating: "))

# Special Case: Purchases above ₹100000 automatically qualify
if purchases > 100000:
    status = "Eligible"
    reason = "Purchase amount exceeded ₹100000."
elif purchases > 50000 and orders >= 20 and rating >= 4.5:
    status = "Eligible"
    reason = "All conditions satisfied."
else:
    status = "Not Eligible"
    reason = "Conditions not met."

# Output
print("Premium Membership Status:", status)
print("Reason:", reason)
