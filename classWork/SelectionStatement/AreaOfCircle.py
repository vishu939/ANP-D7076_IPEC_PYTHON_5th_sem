import math

# Input
radius = float(input("Enter radius of circle: "))

# Validation
if radius <= 0:
    print("Invalid radius! Radius must be positive.")
else:
    area = math.pi * radius * radius
    print("Area of Circle =", area)
