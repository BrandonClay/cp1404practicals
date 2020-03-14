def main():

    user_password = get_password()
    asterisks_output(user_password)

def get_password():
    user_password = input("Please enter a password of at least 3 characters: ")
    while len(user_password) < 3:
        print("That's less than three!")
        user_password = input("Please enter a password of at least 3 characters")
    return user_password

def asterisks_output(user_password):
    for i in range(len(user_password)):
        print("*", end="")

main()