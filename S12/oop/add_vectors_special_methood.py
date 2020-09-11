import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        temp = self.x ** 2 + self.y ** 2
        result = math.sqrt(temp)
        return result

    def __add__(self, other):
        x_temp = self.x + other.x
        y_temp = self.y + other.y
        return Vector(x_temp, y_temp)

    def __mul__(self, other):
        pass



v1 = Vector(4, 3)
v2 = Vector(12, 5)
v3 = v1 + v2
value = v1 * v2
# v3 = v1.__add__(v2)

print(v3.x, v3.y, v3.length())


a = 10
b = 20
c = a + b
c = a.__add__(b)