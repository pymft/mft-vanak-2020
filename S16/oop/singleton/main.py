class Singleton:
    instance = []

    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self):
        self.instance.append(self)


a = Singleton()
b = Singleton()

print(id(a))
print(id(b))