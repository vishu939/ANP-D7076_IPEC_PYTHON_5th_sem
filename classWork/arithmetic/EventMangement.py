# Program to calculate amount per participant

# Input values
total_cost = float(input("Enter the total event cost: "))
participants = int(input("Enter the number of participants: "))

# Calculate amount per participant
amount_per_person = total_cost / participants

# Output
print("Amount per Participant: ₹", amount_per_person)
