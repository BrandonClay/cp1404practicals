
hex_colours = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff", "beige": "#f5f5dc", "black": "#000000", "blue1": "#0000ff", "BlueViolet": "#8a2be2",
               "brown": "#a52a2a", "burlywood": "#deb887"}

user_colour = input("Enter a colour name: ").upper()

while user_colour != "":
    if user_colour in hex_colours:
        print()