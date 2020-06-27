class Temperature:
    def __init__(self, c):
        self.celsius = c

    @property
    def fahrenheit(self):
        return (self.celsius * 1.8) + 32

    # fahrenheit = property(fahrenheit())

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (self.celsius - 32) * (5/ 9)