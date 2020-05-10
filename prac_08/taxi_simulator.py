from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    bill = 0
    taxis = [Taxi("Normal Taxi", 100), SilverServiceTaxi("Cool Silver Taxi", 100, 4),
             SilverServiceTaxi("Cool Limo", 100, 8)]

    menu = "q)uit, c)hoose taxi, d)rive"
    current_taxi = None
    print("lets drive!")
    print(menu)
    menu_choice = input(">>>").upper()

    while menu_choice != "Q":
        if menu_choice == "C":
            print("Taxis available:")
            taxi_display(taxis)
            taxi_choice = int(input("Choose taxi:"))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "D":
            current_taxi.start_fare()
            distance = float(input("Drive how far?"))
            current_taxi.drive(distance)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip costed you ${:.2f}".format(current_taxi.name, trip_cost))
            bill = bill + trip_cost

        else:
            print("try again")
        print("Bill to date: ${:.2f}".format(bill))
        print(menu)
        menu_choice = input(">>>").upper()

    print("Total trips cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    taxi_display(taxis)


def taxi_display(taxis):
    for i, taxi in enumerate(taxis):
        print("{}) - {}".format(i, taxi))


main()
