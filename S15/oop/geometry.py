class Square:
    def __init__(self, a):
        self.side = a

    @property
    def area(self):
        return self.side * self.side

    @property
    def perimeter(self):
        return self.side * 4


