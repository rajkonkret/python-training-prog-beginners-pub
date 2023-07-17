# zbiór (ang. set) - modyfikowalna struktura danych przechowująca niepowtarzające się
# elementy bez informacji o kolejności
from typing import Set

numbers: list[int] = [44, 55, 66, 128, 44, 11, 55, 44]

numbers_set: set[int] = set(numbers)
print(numbers)
print(numbers_set)

for number in numbers_set:
    print(number)

numbers_set_from_literal: set[int] = {29, 50, 29, 100, 55, 128}
print(numbers_set_from_literal)

numbers_set_from_literal.add(120)
print(numbers_set_from_literal)
print(numbers_set_from_literal.pop())
print("=========")
print(numbers_set)
print(numbers_set_from_literal)

print(numbers_set | numbers_set_from_literal)  # suma zbiorów
print(numbers_set & numbers_set_from_literal)  # część wspólna zbiorów
print(numbers_set - numbers_set_from_literal)  # różnica zbiorów
print(numbers_set.union(numbers_set_from_literal))  # suma zbiorów

