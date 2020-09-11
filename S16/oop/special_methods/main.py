class Square:
    def __init__(self, a):
        self.side = a

    @property
    def area(self):
        return self.side * self.side

    def __repr__(self):
        return "SQUARE " + str(self.side) + " x " + str(self.side)


sq = Square(10)
print(sq.side, sq.area)

print(sq)
