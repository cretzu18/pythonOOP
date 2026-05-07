# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self, name, rings, moons, distance_from_sun):
        self.name = name
        self.rings = rings
        self.moons = moons
        self.distance_from_sun = distance_from_sun

    def __str__(self):
        return f"The {self.name} Planet has {self.rings} rings, {self.moons} moons and is {self.distance_from_sun} million kms away from the sun"


if __name__ == "__main__":
    earth = Planet("Eath", 0, 1, 149.6)
    print(earth)
