
hex_colours = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff", "beige": "#f5f5dc", "black": "#000000", "blue1": "#0000ff", "blueviolet": "#8a2be2",
               "brown": "#a52a2a", "burlywood": "#deb887"}

user_colour = input("Enter a colour name: ")
while user_colour != "":
    if user_colour in hex_colours:
        print(hex_colours[user_colour])
        user_colour = input("Enter a colour name: ")
    else:
        print("Invalid colour, try again!")
        user_colour = input("Enter a colour name: ")