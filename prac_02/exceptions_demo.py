"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When anything other than a number is input to  the variables


2. When will a ZeroDivisionError occur?
When the input for the denominator variable is 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
You cannot divide by zero so to avoid the ZeroDivisionError you would have to change the code to NOT do the division
when a 0 is input.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")