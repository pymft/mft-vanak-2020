class Rectangle:
    def __init__(self, a, b):
        self.width = a
        self.height = b

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return (self.width + self.height) * 2


sq1 = Rectangle(4, 5)
sq2 = Rectangle(5, 10)

x = sq1.calculate_area()