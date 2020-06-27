
class Fahrenheit:
    def __get__(self, instance, owner):
        return (instance.value * 1.8) + 32

    def __set__(self, instance, value):
        instance.value = (instance.celsius - 32) * (5 / 9)


class Celsius:
    def __get__(self, instance, owner):
        return instance.value

    def __set__(self, instance, value):
        instance.value = value


class Temperature:
    fahrenheit = Fahrenheit()
    celsius = Celsius()

    def __init__(self):   # we're going to delete this method
        self.value = None


t = Temperature()
t.celsius = 30
print(t.celsius, t.fahrenheit, t.kelvin)