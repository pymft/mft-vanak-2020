class Square:
    def __init__(self, a):
        self.area = a * a
        self.perimeter = 4 * a


sq1 = Square(4)
sq2 = Square(5)

print(sq1.area, sq1.perimeter)
print(sq2.area, sq2.perimeter)