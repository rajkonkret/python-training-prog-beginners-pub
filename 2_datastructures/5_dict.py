# słownik (ang. dictionary) - modyfikowalna struktura danych przechowująca
# pary klucz-wartość
from typing import Dict

my_dict: dict[str, any] = dict()
print(type(my_dict))


my_dict["imie"] = "Marcin"
print(my_dict)
my_dict["imie"] = "Jacek"
print(my_dict)
my_dict["wiek"] = 30
print(my_dict)

print(my_dict.keys())
print(my_dict.values())

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

print(list(my_dict.keys()))  # mamy tu listę kluczy słownika

for key, value in my_dict.items():
    print(f"Klucz: {key}, wartość: {value}")

# print(my_dict["not_found"])  # rzuci to wyjątkiem KeyError, ponieważ klucz not_found nie jest obecny
print(my_dict.get("not_found"))  # zwróci None, ponieważ nie ma takiego klucza
print(my_dict.get("not_found", "default_value"))  # zwróci default_value, ponieważ nie ma takiego klucza


dict_from_literal: dict[str, int] = {"key": 120, "second_key": 440}
print(dict_from_literal)

print({})
print(type({}))  # Jest to pusty słownik

print(set())  # Tak można stworzyć pusty zbiór


