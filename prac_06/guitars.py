from prac_06.guitar import Guitar


def main():
    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $ "))
        guitars.append(Guitar(name, year, cost))
        print(Guitar(name, year, cost), "added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        i = 0
        print("These are my guitars: ")
        for guitar in guitars:
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
                print("Guitar {}: {} ({}), worth ${:5,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                     vintage_string))

            else:
                print(("Guitar {}: {} ({}), worth ${:5,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                      vintage_string)))
            i = i + 1


main()
