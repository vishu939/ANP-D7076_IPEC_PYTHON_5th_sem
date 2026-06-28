# Cybersecurity Login Validation

username = input("Enter Username: ")
password = input("Enter Password: ")
otp = input("Enter OTP: ")

# Stored correct credentials
correct_username = "admin"
correct_password = "admin123"
correct_otp = "4567"

# Username check
if username != correct_username:
    print("User Not Found ❌")
else:
    # Password attempts
    attempts = 1
    while password != correct_password and attempts < 3:
        print("Incorrect Password. Try again.")
        password = input("Enter Password: ")
        attempts += 1

    if password != correct_password:
        print("Account Locked 🔒")
    else:
        # OTP check
        if otp != correct_otp:
            print("Incorrect OTP. Please re-enter OTP 🔄")
        else:
            print("Login Successful ✅")
            print("Welcome Admin")
