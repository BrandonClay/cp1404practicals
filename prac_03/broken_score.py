"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = calculate_result(score)
    print(result)

    random_score = random.randint(0, 100)
    result = calculate_result(random_score)
    print(random_score, result)

def calculate_result(score):
    if score < 0:
        return("Invalid score")
    elif score > 100:
        return ("Invalid score")
    elif score > 50 and score < 90:
        return("Passable")
    elif score > 90:
        return("Excellent")
    else:
        return("Bad")

main()