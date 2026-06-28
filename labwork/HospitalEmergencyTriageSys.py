# Hospital Emergency Triage System

critical = input("Critical Condition (Y/N): ")
age = int(input("Enter Age: "))
oxygen = int(input("Enter Oxygen Level: "))

priority = ""
reason = ""

# Step 1: Critical condition check
if critical.upper() == "Y":
    priority = "Immediate Treatment"
    reason = "Critical Condition"
elif oxygen < 90:
    priority = "High Priority"
    reason = "Low Oxygen Level"
elif age > 65:
    priority = "Medium Priority"
    reason = "Senior Citizen"
else:
    priority = "Normal Priority"
    reason = "Stable Condition"

# Output
print("Patient Priority:", priority)
print("Reason:", reason)
