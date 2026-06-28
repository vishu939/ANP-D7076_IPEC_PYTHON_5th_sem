# University Scholarship System

percentage = int(input("Enter Percentage: "))
income = int(input("Enter Family Income: "))
disciplinary = input("Disciplinary Action (Y/N): ")

# Scholarship Logic
scholarship = 0
reason = ""

if income >= 800000:
    scholarship = 0
    reason = "Family income exceeds ₹8,00,000."
elif disciplinary.upper() == "Y":
    scholarship = 0
    reason = "Disciplinary action recorded."
else:
    if percentage >= 95:
        scholarship = 100
    elif percentage >= 90:
        scholarship = 75
    elif percentage >= 85:
        scholarship = 50
    elif percentage >= 80:
        scholarship = 25
    else:
        scholarship = 0
        reason = "Percentage below 80."

# Output
if scholarship > 0:
    print("Scholarship Awarded:", str(scholarship) + "%")
else:
    print("Scholarship Awarded: No Scholarship")
    print("Reason:",reason)