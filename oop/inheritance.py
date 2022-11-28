class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    # overriding init method of the base class(Stream)
    def __init__(self):
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)

even_numbers = []
