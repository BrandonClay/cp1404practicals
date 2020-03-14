user_pass = input("Please enter a password of at least 3 characters: ")

while len(user_pass) < 3:
    print("That's less than three!")
    user_pass = input("Please enter a password of at least 3 characters")

for i in range(len(user_pass)):
    print("*", end="")