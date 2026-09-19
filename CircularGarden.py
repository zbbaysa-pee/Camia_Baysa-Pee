# Import math so that the math libraries will be accessible
import math

# Collect values for computation
radius = float(input("Enter radius: "))

# Calculate the values using math.pow(), math.pi, math.sqrt(), math.floor(), and math.ceil()
area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius
square_root = math.sqrt(area)
area_rounded_down = math.floor(area)
area_rounded_up = math.ceil(area)

# Display the results, making the area, circumference, and square root rounded to two decimal places
print(f"Area of the garden: {area:.2f} square meters")
print(f"Circumference of the garden: {circumference:.2f} meters")
print(f"Square_root of the area: {square_root:.2f}")
print("Area rounded down: ", area_rounded_down, "square meters")
print("Area rounded up: ", area_rounded_up, "square meters")

