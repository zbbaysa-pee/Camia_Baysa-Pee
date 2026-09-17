try:
    score = int(input("Enter examination score: "))
    if 0 <= score <= 100:
        print("Valid score.")
    else:
        print("Invalid score.")
except ValueError:
    print("Invalid input. Please enter a number.")
