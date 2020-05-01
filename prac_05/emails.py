
def main():

    email_and_names = {}
    email = input("Enter email: ")
    
    while email != "":
        name = name_from_email(email)
        name_check = input("Is your name {}? (y/n) ".format(name))
        
        if name_check.upper() != "Y" and name_check != "":
            name = input("Whats your name? ")
        email_and_names[email] = name
        email = input("Enter email: ")

    for email, name in email_and_names.items():
        print("{} ({})".format(name, email))


# function that gets the users name from the email.
def name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
