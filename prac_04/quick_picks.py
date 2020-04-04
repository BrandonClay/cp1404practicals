import random

line_size = 6
minimum = 1
maximum = 45

quick_picks = []
number_of_picks = int(input("How many quick picks? "))

for i in range (number_of_picks):
    for j in range (line_size):
        number = random.randint(minimum, maximum )
        quick_picks.append(number)
print(quick_picks)

#struggled with working this one out sorry