# Recharge program using user choice directly

packs = {
    1: "₹199 Pack",
    2: "₹249 Pack",
    3: "₹299 Pack"
}

print("Available Packs:")
for key, value in packs.items():
    print(key, ":", value)

choice = int(input("Enter pack number: "))

print("Recharge Amount:", packs.get(choice, "Invalid choice"))
