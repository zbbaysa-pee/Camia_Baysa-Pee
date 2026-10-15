# Get number values (global variables)
number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))

# Calculate the sum of the first and second number (the sum will be a local variable)
def calculate_sum ():
    sum = number_one + number_two
    print(f"Sum: {sum}")
# Calculate the difference of the first and second number (the difference will be a local variable)
def calculate_difference ():
    difference = number_one - number_two
    print(f"Difference: {difference}")

calculate_sum()
calculate_difference()
