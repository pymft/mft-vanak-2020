class Area:
    def __get__(self, instance, owner):
        return instance.side * instance.side


class Perimeter:
    def __get__(self, instance, owner):
        return instance.side * 4


class Square:
    area = Area()
    perimeter = Perimeter()

    def __init__(self, a):
        self.side = a
