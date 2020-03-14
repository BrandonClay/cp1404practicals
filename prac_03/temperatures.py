"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
                celsius = convert_to_fahrenheit()
                print("Result: {:.2f} F".format(celsius))
        elif choice == "F":
                fahrenheight = convert_to_celsius()
                print("Result: {:.2f} F".format(fahrenheight))
        else:
                print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def convert_to_fahrenheit():
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        return fahrenheit

def convert_to_celsius():
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        return celsius

main()