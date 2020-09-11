import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        temp = self.x * self.x + self.y * self.y
        result = math.sqrt(temp)
        return result


def add_vectors(a: Vector, b: Vector) -> Vector:
    x_temp = a.x + b.x
    y_temp = a.y + b.y
    return Vector(x_temp, y_temp)


v1 = Vector(4, 3)
v2 = Vector(12, 5)
v3 = add_vectors(v1, v2)

print(v3.x, v3.y, v3.length())
