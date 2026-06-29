# Shopping Cart Billing System

# Input: number of products
n = int(input("Enter number of products: "))

products = []   # List to store product details
costs = []      # List to store individual product costs

# Accept product details
for i in range(n):
    name = input(f"\nEnter name of product {i+1}: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    
    # Calculate cost for this product
    cost = qty * price
    
    # Store details
    products.append((name, qty, price, cost))
    costs.append(cost)

# Calculate required values
total_bill = sum(costs)
average_cost = total_bill / n

# Find most expensive and cheapest product
most_expensive = max(products, key=lambda x: x[3])   # based on cost
cheapest = min(products, key=lambda x: x[3])         # based on cost

# Display results
print("\n--- Shopping Cart Analysis ---")
for p in products:
    print(f"{p[0]} → Quantity: {p[1]}, Unit Price: {p[2]}, Cost: {p[3]}")

print("\nTotal Bill Amount:", total_bill)
print("Average Product Cost:", average_cost)
print("Most Expensive Product:", most_expensive[0], "with cost", most_expensive[3])
print("Cheapest Product:", cheapest[0], "with cost", cheapest[3])
