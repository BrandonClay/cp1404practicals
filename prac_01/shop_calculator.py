total_price = 0
num_items = int(input("Number of Items: "))
while num_items < 0:
    print("Invalid number of items.")
    num_items = int(input("Number of Items: "))
for i in range(num_items):
    item_price = float(input("Price of Item: "))
    total_price += item_price

if total_price > 100:
    total_price = total_price * 0.9

