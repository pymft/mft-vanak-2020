import math

class Parallelogram:
    def __init__(self, a, b, c):
        self.width = a
        self.height = b
        self.angle = c

    @property
    def area(self):
        return self.width * self.height * math.sin(self.angle)

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

class Diamond(Parallelogram):
    def __init__(self, a, c):
        self.width = a
        self.height = a
        self.angle = c


class Rectangle(Parallelogram):
    def __init__(self, a, b):
        self.width = a
        self.height = b
        self.angle = math.pi/2


class Square(Rectangle):
    def __init__(self, a):
        self.width = a
        self.height = a
        self.angle = math.pi/2




sq = Square(10)
print(sq.width, sq.height, sq.area, sq.perimeter)

rect = Rectangle(3, 5)
print(rect.width, rect.height, rect.area, rect.perimeter)

diamond = Rectangle(3, 5)
print(diamond.width, diamond.height, diamond.area, diamond.perimeter)

par = Parallelogram(3, 5, math.pi/6)
print(par.width, par.height, par.area, par.perimeter)