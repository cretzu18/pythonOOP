# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Chair:
    def __init__(self, color, price, amount):
        self.color = color
        self.price = price
        self.amount = amount

    def __str__(self):
        return f"We have {self.amount} {self.color} chairs and they cost {self.price}$."
    
    def __add__(self, other):
        if self.amount >= other.amount:
            new_color = self.color
        else:
            new_color = other.color

        new_price = self.price + other.price
        new_amount = self.amount + other.amount

        return Chair(new_color, new_price, new_amount)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} written by {self.author} has {self.pages} pages."
    
    def __add__(self, other):
        new_title = self.title + ", " + other.title
        new_author = self.author + ", " + other.author
        new_pages = self.pages + other.pages

        return Book(new_title, new_author, new_pages)

class Phone:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"The {self.model} phone from {self.year} costs {self.price}$."
    
    def __add__(self, other):
        if self.price >= other.price:
            new_model = self.model
            new_year = self.year
        else:
            new_model = other.model
            new_year = other.year

        new_price = self.price + other.price

        return Phone(new_model, new_year, new_price)


if __name__ == "__main__":
    chair1 = Chair("red", 100, 2)
    chair2 = Chair("yellow", 300, 5)
    print(chair1 + chair2)

    book1 = Book("Amazing title", "Amazing author", 420)
    book2 = Book("Another amazing title", "Another amazing author", 300)
    print(book1 + book2)

    phone1 = Phone("iPhone", 2024, 1000)
    phone2 = Phone("Samsung", 2025, 800)
    print(phone1 + phone2)