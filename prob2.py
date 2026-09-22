# Y'Draelle Agas, Ivanka Barrozo, Ziva Baysa-Pee
# 8-Camia

username = str(input("Enter username: "))

# Limit username length to 5-10 characters inclusive and use .isalnum so only numbers and letters are accepted
if 5 <= len(username) <= 10 and username.isalnum():
    print("Valid username.")
else:
    print("Invalid username.")