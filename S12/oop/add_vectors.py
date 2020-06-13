import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        temp = self.x ** 2 + self.y ** 2
        result = math.sqrt(temp)
        return result

    def add_to_another_vector(self, other):
        x_temp = self.x + other.x
        y_temp = self.y + other.y
        return Vector(x_temp, y_temp)


v1 = Vector(4, 3)
v2 = Vector(12, 5)
v3 = v1.add_to_another_vector(v2)

print(v3.x, v3.y, v3.length())
