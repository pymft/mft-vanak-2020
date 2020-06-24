class Extrude:
    @property
    def volume(self):
        return self.area * self.height


class Square:
    def __init__(self, a):
        self.a = a

    @property
    def area(self):
        return self.a * self.a


class Circle:
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return self.r * self.r * 3.1415


class Cube(Square, Extrude):
    def __init__(self, a):
        super().__init__(a)
        self.height = a


class Cylinder(Circle, Extrude):
    def __init__(self, r):
        super().__init__(r)
        self.height = a




c = Cylinder(10)
print(c.volume)