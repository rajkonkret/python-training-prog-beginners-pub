class Celsius:
    def __init__(self, temperature: float = 0):
        self.temperature = temperature

    def to_fahrenheit(self) -> float:
        return (self.temperature * 1.8) + 32



class Celsius:
    def __init__(self, temperature: float = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self) -> float:
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self) -> float:
        return self._temperature

    # setter method
    def set_temperature(self, value) -> None:
        if value < -273.15:
            raise ValueError("Temperatura poniżej 273.15 jest niedopuszczalna")
        self._temperature = value


human: Celsius = Celsius(37)

print(human.get_temperature())
print(human.to_fahrenheit())
# human.set_temperature(-300)
print(human.to_fahrenheit())


# Dekorator property
class Celsius:
    def __init__(self, temperature: float = 0):
        self._temperature: float = temperature

    def to_fahrenheit(self) -> float:
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# coldest_thing: Celsius = Celsius(-300)

class Temperature:
    def __secret_method(self):
        pass


print(dir(Temperature()))

Temperature()._Temperature__secret_method()

