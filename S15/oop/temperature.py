class Celsius:
    def __set__(self, instance, value):
        instance.value = value

    def __get__(self, instance, owner):
        return instance.value


class Fahrenheit:
    def __set__(self, instance, value):
        instance.value = (instance.celsius - 32) * (5 / 9)

    def __get__(self, instance, owner):
        return (instance.value * 1.8) + 32


class Temperature:
    celsius = Celsius()
    fahrenheit = Fahrenheit()


t = Temperature()
t.celsius = 30
print(t.celsius, t.fahrenheit)