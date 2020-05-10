from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    cool_taxi = SilverServiceTaxi("Cool Taxi", 100, 2)
    cool_taxi.drive(50)

    print(cool_taxi.get_fare())
    print(cool_taxi)


main()
