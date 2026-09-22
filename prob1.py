# Y'Draelle Agas, Ivanka Barrozo, Ziva Baysa-Pee
# 8-Camia

try:
    age = int(input("Enter your age: "))
    if 12 <= age <= 18:
        print("Valid age")
    else:
        print("Invalid age. Age must be from 12 to 18.")
except ValueError:
    print("Invalid age. Please enter a whole number.")