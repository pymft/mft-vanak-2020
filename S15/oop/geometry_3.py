# مستطیل
class Area:
    def __get__(self, instance, owner):
        return instance.width * instance.height


class Perimeter:
    def __get__(self, instance, owner):
        return (instance.width + instance.height) * 2


class Rectangle:
    area = Area()
    perimeter = Perimeter()

    def __init__(self, a, b):
        self.width = a
        self.height = b


rect = Rectangle(10, 4)
print(rect.perimeter, rect.area)
