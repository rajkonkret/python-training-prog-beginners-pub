# bez type hint funkcja wyglądałaby tak: def my_function():
import datetime
from typing import List


def my_function() -> None:
    pass


print(my_function())


#
# def divide(number):
#     return number // 2


def divide(number: int) -> int:
    return number // 2


print(divide(2))


def divide(arg: str) -> str:
    return arg[:len(arg) // 2]


print(divide("string"))


# print(divide(5))  # to nie zadziała, ponieważ ponowna deklaracja funkcji divide przesłoniła poprzednią


def divide(arg: int | str) -> int | str:
    if isinstance(arg, int):
        return arg // 2
    elif isinstance(arg, str):
        return arg[:len(arg) // 2]
    else:
        raise ValueError


print(divide("string"))
print(divide(5))


# print(divide(datetime.date.today()))  rzuci wyjątkiem - wykona się blok else


def divide(arg: int | str, divider: int) -> int | str:
    if isinstance(arg, int):
        return arg // divider
    elif isinstance(arg, str):
        return arg[:len(arg) // divider]


# print(divide("string"))  # Nie zadziała, pomimo zdefiniowania funkcji o tejsamej nazwie, ale innej liczbie argumentów
print(divide("string", 2))


# bez type hint definicja rozpoczynałaby się od: def divide(arg, divider = 2)
def divide(arg: int | str, divider: int = 2) -> int | str:
    if isinstance(arg, int):
        return arg // divider
    elif isinstance(arg, str):
        return arg[:len(arg) // divider]


print(divide("string"))  # teraz zadziała
print(divide("string", 2))

print(divide(arg=150, divider=2))  # keword arguments
# print(divide(arg=150, 2))  # keword arguments muszą pojawić się na końcu
print(divide(150, divider=2))  # keword arguments muszą pojawić się na końcu
print(divide(divider=2, arg=150))

arg_list = [150, 3]
print(divide(arg_list[0], arg_list[1]))
print(divide(*arg_list))  # zadziała jak linijka wyżej dla dowolnej liczby argumentów


def list_updater(my_list: list = []) -> list:
    my_list.append("surprise")
    return my_list


my_list: list[int] = [1, 2]
print(list_updater(my_list))  # typy mutowalne są przekazywane przez referencję
print(my_list)  # my_list zostało zmodyfikowane

print(list_updater())
print(list_updater())
print(id(list_updater()))
print(id(list_updater()))  # dodajemy element do tej samej listy, która zosta stworzona w momencie,


# gdy interpreter pythona dotarł do definicji funkcji


def list_updater(my_list=None) -> list:
    if my_list is None:
        my_list = []
    my_list.append("surprise")
    return my_list


print(list_updater())
print(list_updater())
print(list_updater())


# funkcje z dowolną liczbą argumentów
def make_tuple(*args) -> tuple[any]:
    print(args)
    print(type(args))  # args - krotka zawierająca argumenty
    return args


make_tuple(1, 2, 5, 8)


def make_dict(**kwargs) -> dict[str, any]:
    print(kwargs)
    print(type(kwargs))
    return kwargs


make_dict(arg1=5, another_argument="string")


def make_tuple_and_dict(*args, **kwargs) -> tuple[tuple[any], dict[str, any]]:
    return make_tuple(*args), make_dict(**kwargs)


print(make_tuple_and_dict(4, arg1=5, another_argument="string"))

# Zasięg zmiennych w funkcji

variable: int = 10


def print_variable() -> None:
    print(variable)  # możemy odwołać się do zmiennej zdefiniowanej poza funkcją


print_variable()


def modify_variable() -> None:
    variable = 1


modify_variable()
print(variable)  # wypisze 10, zmienna globalna variable nie zostanie zmodyfikowana


def modify_variable() -> None:
    global variable  # bez tego utowrzy się lokalna zmienna variable
    variable = 1


modify_variable()
print(variable)  # wypisze 1, zmienna globalna variable zostanie zmodyfikowana


def calculator(number: int) -> tuple[int, int]:
    multiplication_result = number * 2
    division_result = number // 2
    return multiplication_result, division_result


print(calculator(5))
_, result = calculator(5)

print(result)  # wipisze wynik dzielenia

