from prac_06.guitar import Guitar
CURRENT_YEAR = 2020


def main():
    name = "Cool guitar"
    year = 1960
    cost = 1000
    guitar_one = Guitar(name, year, cost)
    guitar_two = Guitar("Guitar two ", 1980, 2000)

    # get_age test
    print("{} get_age() -expected {}, got {}".format(guitar_one.name, 60, guitar_one.get_age()))
    print("{} get_age() -expected {}, got {}".format(guitar_two.name, 40, guitar_two.get_age()))

    # is_vintage test
    print("{} is_vintage() - Expected {}. Got {}".format(guitar_one.name, True, guitar_one.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar_two.name, False, guitar_two.is_vintage()))


main()
