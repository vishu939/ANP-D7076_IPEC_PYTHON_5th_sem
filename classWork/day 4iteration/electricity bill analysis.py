# Electricity Bill Analysis for N houses

# Input: number of houses
N = int(input("Enter number of houses: "))

# List to store units
units = []

# Accept monthly units consumed by each house
for i in range(N):
    u = int(input(f"Enter units consumed by house {i+1}: "))
    units.append(u)

# Calculate required values
total_units = sum(units)
average_units = total_units / N
highest_units = max(units)
lowest_units = min(units)

# Display results
print("\nElectricity Consumption Analysis:")
print("Total units consumed:", total_units)
print("Average units consumed:", average_units)
print("Highest consumption:", highest_units)
print("Lowest consumption:", lowest_units)
