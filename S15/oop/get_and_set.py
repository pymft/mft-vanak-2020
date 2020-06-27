class Temperature:
    def __init__(self, c):
        self.celsius = c

    @property
    def fahrenheit(self):
        return (self.celsius * 1.8) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * (5 / 9)


t = Temperature(30)
print(t.celsius, t.fahrenheit)
t.celsius = 40
print(t.celsius, t.fahrenheit)
t.fahrenheit = 100
print(t.celsius, t.fahrenheit)
