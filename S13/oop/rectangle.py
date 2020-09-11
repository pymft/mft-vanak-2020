import math


class Rectangle:
    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def area(self):
        return self.width * self.height

    @area.setter
    def area(self, value):
        ratio = math.sqrt(value / self.area)

        self.width = self.width * ratio
        self.height = self.height * ratio

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    @perimeter.setter
    def perimeter(self, value):
        ratio = value / self.area

        self.width = self.width * ratio
        self.height = self.height * ratio


rect = Rectangle(1, 5)
print(rect.width, rect.height, rect.area, rect.perimeter)

rect.area = 20
print(rect.width, rect.height, rect.area, rect.perimeter)

rect.perimeter = 40
print(rect.width, rect.height, rect.area, rect.perimeter)