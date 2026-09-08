import math

# Ask the user for the values
sideA = float(input("Enter the length of side A: "))
sideB = float(input("Enter the length of side B: "))

# Calculate for the hypotenuse using sqrt() and pow()
sideC = math.sqrt(pow(sideA, 2) + pow(sideB, 2))

# Display the result
print(f"The hypotenuse is: {sideC:.2f}")