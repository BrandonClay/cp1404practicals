from prac_08.unreliable_car import UnreliableCar


def main():
    car = UnreliableCar("Cool Car", 100, 50)

    for i in range(5):
        # If the print says drove 0 it means the car failed to drive that iteration
        print("car {} drove {}".format(i + 1, car.drive(i)))


main()
