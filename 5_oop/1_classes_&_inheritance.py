class A:
    pass


a: A = A()

print(type(a))


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def print_full_name(self) -> None:
        print(f"{self.name} {self.surname}")

    def __str__(self):
        return f"{self.name} {self.surname}"


john: Person = Person("John", "Kowalski")
print(john.name)
print(john.surname)

john.print_full_name()
print(john)


class Car:
    def __init__(self, owner: Person, brand: str, colour: str = "black", max_speed: int = 100):
        self.owner = owner
        self.colour = colour
        self.brand = brand
        self.max_speed = max_speed

    def run(self):
        for _ in range(self.max_speed // 20):
            print("Wrrrr")

    def print_owner(self):
        print(self.owner)

    def __str__(self):
        return f"{self.owner}, {self.brand}, {self.colour}, {self.max_speed}"

    @staticmethod
    def some_static() -> str:
        return "I am static method"


ford_car: Car = Car(john, "Ford")
print(ford_car.max_speed)
ford_car.run()
print(ford_car)
print(Car.some_static())
print(ford_car.some_static())


class Ford(Car):
    def __init__(self, owner: Person, colour: str = "black", max_speed: int = 100):
        super().__init__(owner, "Ford", colour, max_speed)


ford_ford: Ford = Ford(john)
print(ford_ford.max_speed)
ford_ford.run()
print(ford_ford)
print(Car.some_static())
print(ford_ford.some_static())

print(isinstance(ford_car, Ford))
print(isinstance(ford_car, Car))
print(isinstance(ford_ford, Ford))
print(isinstance(ford_ford, Car))


class A:
    pass


class B(A):
    pass


class C(B, A):
    pass


print(C.__mro__)  # wipisze kolejność, w jakiej sprawdzamy możliwość wywołania poszczególnych metod, czy pól


# class D(B, C):  # Nie każda kombinacja wielokrotnego dziedziczenia ma szansę zadziałać przy wyznaczaniu mro - method resolution order
#     pass

