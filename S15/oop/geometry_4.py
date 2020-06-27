class Area:
    def __get__(self, instance, owner):
        if owner == Square:
            return instance.side * instance.side
        elif owner == Rectangle:
            return instance.width * instance.height
        elif owner == Circle:
            return instance.radius * instance.radius * 3.14


class Perimeter:
    def __get__(self, instance, owner):
        if owner == Square:
            return instance.side * 4
        elif owner == Rectangle:
            return (instance.width + instance.height) * 2
        elif owner == Circle:
            return 2 * instance.radius * 3.14


class Square:
    area = Area()
    perimeter = Perimeter()

    def __init__(self, a):
        self.side = a


class Rectangle:
    area = Area()
    perimeter = Perimeter()

    def __init__(self, a, b):
        self.width = a
        self.height = b


class Circle:
    area = Area()
    perimeter = Perimeter()

    def __init__(self, r):
        self.radius = r



sq = Square(10)
rect = Rectangle(2, 5)
circle = Circle(10)
print("square:", sq.perimeter, sq.area)
print("rectangle", rect.perimeter, rect.area)
print("circle:", circle.perimeter, circle.area)