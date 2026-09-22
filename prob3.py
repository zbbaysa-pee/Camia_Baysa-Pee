# Y'Draelle Agas, Ivanka Barrozo, Ziva Baysa-pee
# 8-Camia

try:
    Grade_Level = int(input("Enter your grade level (7-10): "))

    if 7 <=  Grade_Level <= 11:
        print("Valid grade level.")
    else:
        print("Invalid grade level.")

except ValueError:
    print("Invalid input. Enter a whole number.")