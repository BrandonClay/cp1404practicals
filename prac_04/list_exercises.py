#1.
# numbers = []
# while len(numbers) < 5:
#     numbers.append(int(input("Number: ")))
#
# print("The first number is {}".format(numbers[0]))
# print("The last number is {}".format(numbers[-1]))
# print("The smallest number is {}".format(min(numbers)))
# print("The largest number is {}".format(max(numbers)))
# print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))

#2.
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username_check = input("Enter username:  ")
if username_check in usernames:
    print("Access Granted")
else:
    print("Access Denied")
