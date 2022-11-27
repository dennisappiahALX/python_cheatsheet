class Point:
    default_colour = "red"

    # can be accessed by all instances and methods of the class

    def __init__(self, x, y):
        # initializing attributes of base objects
        self.x = x
        self.y = y

    def draw(self):
        print(f"{self.x} {self.y}")

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


Point.default_colour = "yellow"

point = Point(1, 2)
another = Point(1, 2)
combined = point + another

print(point == another)

print(combined.x)
print(point.default_colour)


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be less tha zero")
        self.__price = value


product = Product(50)
product.price = 4
print(product.price)
