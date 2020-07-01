
class Square:
    instances = []

    def __init__(self, a):
        self.side = a
        self.instances.append(self)

    def area(self):
        return self.side * self.side

    def __repr__(self):
        return "SQUARE:" + str(self.side) + "x" + str(self.side)

    @classmethod
    def count(cls):
        return len(cls.instances)


sq1 = Square(10)
print(sq1.count())
sq2 = Square(20)
sq3 = Square(22)
print(Square.count())
