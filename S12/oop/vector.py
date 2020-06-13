import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        temp = self.x ** 2 + self.y ** 2
        result = math.sqrt(temp)
        return result


v1 = Vector(4, 3)
v2 = Vector(12, 5)


print(v1.x, v1.y, v1.length())
print(v2.x, v2.y, v2.length())