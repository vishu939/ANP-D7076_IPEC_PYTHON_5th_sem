# Login System with Maximum Attempts

correct_username = "admin"      # Stored correct username
correct_password = "python123"  # Stored correct password

attempts = 0   # Counter to track number of attempts

while attempts < 3:   # Loop runs until 3 attempts
    print(f"Attempt {attempts + 1}")   # Show current attempt number
    username = input("Username: ")     # Take username input
    password = input("Password: ")     # Take password input

    # Check if both username and password are correct
    if username == correct_username and password == correct_password:
        print("\nLogin Successful ")   # Success message
        break   # Exit loop if login successful
    else:
        print("\nInvalid Credentials \n")   # Error message
        attempts += 1   # Increase attempt count

# If 3 wrong attempts → account locked
if attempts == 3:
    print("Account Locked ")
