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
        super().__init__(a, a, c)


class Rectangle(Parallelogram):
    def __init__(self, a, b):
        super().__init__(a, b,  math.pi/2)


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)




sq = Square(10)
print(sq.width, sq.height, sq.area, sq.perimeter)

rect = Rectangle(3, 5)
print(rect.width, rect.height, rect.area, rect.perimeter)

diamond = Rectangle(3, 5)
print(diamond.width, diamond.height, diamond.area, diamond.perimeter)

par = Parallelogram(3, 5, math.pi/6)
print(par.width, par.height, par.area, par.perimeter)