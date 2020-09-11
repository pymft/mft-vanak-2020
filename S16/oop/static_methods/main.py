import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    @staticmethod
    def calculate_length(x, y):
        return math.sqrt(x * x + y * y)


v1 = Vector(3, 4)
print(v1.length())
print(v1.calculate_length(12, 5))