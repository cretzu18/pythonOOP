# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def increase_max_speed(self):
        self.max_speed += 5

    def show(self):
        print(f"{self.model} from {self.year} has a max speed of {self.max_speed} kms/hour.")


if __name__ == "__main__":
    dacia = Car("Dacia", 1999, 120)
    vw = Car("Passat", 2005, 180)
    dacia.show()
    vw.show()

    dacia.increase_max_speed()
    dacia.increase_max_speed()
    dacia.increase_max_speed()

    vw.increase_max_speed()

    dacia.show()
    vw.show()