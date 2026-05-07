# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


if __name__ == "__main__":
    rect = Rectangle(4, 5)
    circle = Circle(10)

    print(f"Area rectangle: {rect.area()}")
    print(f"Perimeter rectangle: {rect.perimeter()}")

    print(f"Area circle: {circle.area()}")
    print(f"Circumference circle: {circle.circumference()}")

