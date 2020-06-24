class MokaabMostatil:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    @property
    def volume(self):
        return self.a * self.b * self.h


class Mokaab(MokaabMostatil):
    def __init__(self, a):
        super().__init__(a, a, a)


m = Mokaab(10)
print(m.volume)

m = MokaabMostatil(2, 5, 10)
print(m.volume)