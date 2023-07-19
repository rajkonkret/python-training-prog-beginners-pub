from abc import ABC, abstractmethod


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def print_full_name(self) -> None:
        print(f"{self.name} {self.surname}")

    def __str__(self):
        return f"{self.name} {self.surname}"


class AbstractCar(ABC):
    def __init__(self, owner: Person, brand: str, colour: str = "black", max_speed: int = 100):
        self.owner = owner
        self.colour = colour
        self.brand = brand
        self.max_speed = max_speed

    @abstractmethod
    def run(self):
        pass

    def print_owner(self):
        print(self.owner)

    def __str__(self):
        return f"{self.owner}, {self.brand}, {self.colour}, {self.max_speed}"

    @staticmethod
    def some_static() -> str:
        return "I am static method"


class Ford(AbstractCar):
    def __init__(self, owner: Person, colour: str = "black", max_speed: int = 100):
        super().__init__(owner, "Ford", colour, max_speed)

    @staticmethod
    def some_static() -> str:
        return "I am another static method"

    def run(self):
        for _ in range(self.max_speed // 20):
            print("Brrrrum")


class Kia(AbstractCar):
    def __init__(self, owner: Person, colour: str = "black", max_speed: int = 100):
        super().__init__(owner, "Kia", colour, max_speed)

    def run(self):
        for _ in range(self.max_speed // 20):
            print("Wrrrr")


john = Person("John", "Kowalski")
kia = Kia(john, "Skoda")

def use_a_car(car: AbstractCar):
    car.run()

use_a_car(kia)
