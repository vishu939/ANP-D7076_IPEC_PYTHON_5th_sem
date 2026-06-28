# Multi-Level Access Control System

role = input("Enter Role (Admin/Manager/Employee/Guest): ")
status = input("Account Status (Active/Inactive): ")

access_level = "No Access"

if status.lower() != "active":
    access_level = "No Access"
else:
    if role.lower() == "admin":
        clearance = int(input("Enter Security Clearance: "))
        if clearance >= 5:
            access_level = "Full Access"
        else:
            access_level = "Limited Admin Access"
    elif role.lower() == "manager":
        experience = int(input("Enter Years of Experience: "))
        if experience > 5:
            access_level = "Department Access"
        else:
            access_level = "Limited Manager Access"
    elif role.lower() == "employee":
        experience = int(input("Enter Years of Experience: "))
        if experience > 2:
            access_level = "Limited Access"
        else:
            access_level = "Basic Employee Access"
    elif role.lower() == "guest":
        access_level = "Read-Only Access"

# Output
print("Access Level:", access_level)
