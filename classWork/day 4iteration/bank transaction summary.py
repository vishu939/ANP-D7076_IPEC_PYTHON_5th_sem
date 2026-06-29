# Bank Transaction Summary

total_deposit = 0
total_withdrawal = 0

print("Enter transactions (positive = deposit, negative = withdrawal, 0 = finish):")

while True:
    amount = int(input("Enter transaction amount: "))
    
    if amount == 0:   # stop condition
        break
    elif amount > 0:
        total_deposit += amount
    else:
        total_withdrawal += abs(amount)  # withdrawal stored as positive value

# Final balance = deposits - withdrawals
final_balance = total_deposit - total_withdrawal

# Display results
print("\nTransaction Summary:")
print("Total Deposit:", total_deposit)
print("Total Withdrawal:", total_withdrawal)
print("Final Balance:", final_balance)
