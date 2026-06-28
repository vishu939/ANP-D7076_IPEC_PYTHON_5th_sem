# Input
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

# Validation
if length <= 0 or width <= 0:
    print("Invalid input! Length and width must be positive.")
else:
    area = length * width
    perimeter = 2 * (length + width)

    print("Area of Rectangle =", area)
    print("Perimeter of Rectangle =", perimeter)
