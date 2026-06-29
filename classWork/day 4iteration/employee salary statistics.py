# Employee Salary Statistics

# Accept number of employees
n = int(input("Enter number of employees: "))

# Initialize variables
salaries = []
total = 0
count_above_50k = 0

# Accept salaries using iteration
for i in range(n):
    salary = float(input(f"Enter salary of employee {i+1}: "))
    salaries.append(salary)
    total += salary
    if salary > 50000:
        count_above_50k += 1

# Calculate statistics
highest = max(salaries)
lowest = min(salaries)
average = total / n

# Display results
print("\n--- Employee Salary Statistics ---")
print("Highest Salary: ₹", highest)
print("Lowest Salary: ₹", lowest)
print("Average Salary: ₹", average)
print("Employees earning more than ₹50,000:", count_above_50k)
