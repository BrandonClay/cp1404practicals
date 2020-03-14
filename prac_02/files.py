
# 1)
# name_file = open("name.txt", "w")
# name_input = str(input("enter name: "))
# print(name_input, file=name_file)
# name_file.close()

# 2)
# name_file = open("name.txt")
# read_name = name_file.read()
# print("your name is ", read_name)

# name_file.close()

# 3)
#numbers_file = open("numbers.txt", "r")
#
# number_one = int(numbers_file.readline())
# number_two = int(numbers_file.readline())
# total = number_one + number_two
# print(total)
#numbers_file.close()

# 4)
numbers_file = open("numbers.txt", "r")
total = 0

for i in numbers_file:
    number = int(i)
    total += number
print(total)

numbers_file.close()