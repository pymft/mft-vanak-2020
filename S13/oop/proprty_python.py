import math


class Square:
    def __init__(self, a):
        self.side = a
        self.__area = self.side * self.side

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        self.side = math.sqrt(value)
        self.__area = self.side * self.side


sq1 = Square(10)
print(sq1.side, sq1.area)

sq1.area = 400
print(sq1.side, sq1.area)