import datetime
from datetime import date
from typing import List

# type-hint w startym stylu
# training_attendants: List[str] = ["Łukasz", "Marcin", "Maciek", "Paulina"]
# type-hint dostępny od pythona 3.9
training_attendants: list[str] = ["Łukasz", "Marcin", "Maciek", "Paulina"]
print(training_attendants)

print(training_attendants[0])
training_attendants[0] = "Jakub"
print(training_attendants)

print(training_attendants[-1])
print(training_attendants[-2])

print("python"[3])
print("python"[-1])

numbers: list[int] = [10, 15, -3, 44, 0, 30, 144, 57, 99]

rubbish: list[any] = [4, 22, None, 3.2, "python", datetime.date.today()]

# slicing
print(numbers[:2])
print(numbers[2:])
print(numbers[1:3])  # elementy o indeksach od 1 do 3 (bez 3)
print(numbers[1:7:2])  # elementy o indeksach of 1 do 7 co drugi
print(numbers[::2])  # co drugi element
print(numbers[::-1])

print("python"[2:4])  # sliicing działa dla typu str

print("Bez copy:")
new_numbers: list[int] = numbers
print(numbers)
print(new_numbers)

new_numbers[2] = -9999
print(numbers)
print(new_numbers)

print(id(numbers))
print(id(new_numbers))  # identyfikatory są takie same; zmienne numbers i new_numbers wskazują na tę samą liste

new_numbers[2] = -3

print("Z użyciem copy:")
print(numbers)
print(new_numbers)
new_numbers = numbers.copy()
new_numbers[2] = -4444

print(numbers)
print(new_numbers)

print(id(numbers))
print(id(new_numbers))  # identyfikatory są różne; zmienne numbers i new_numbers wskazują na tę samą liste

new_numbers[2] = -3

print("Slicing:")
print(numbers)
new_numbers = numbers[:5]  # tworzy zupełnie nową listę
print(new_numbers)
new_numbers[2] = -4444

print(numbers)  # elementy pozostają niemzienione
print(new_numbers)

print("Lista list:")
list_of_lists: list[list[int]] = [[1, 2], [3, 4]]
print(list_of_lists)
new_lists_of_lists: list[list[int]] = list_of_lists
print(new_lists_of_lists)

new_lists_of_lists[1][1] = 100
print(list_of_lists)
print(new_lists_of_lists)

new_lists_of_lists[1][1] = 4

print("Lista list (copy):")
list_of_lists: list[list[int]] = [[1, 2], [3, 4]]
print(list_of_lists)
new_lists_of_lists: list[list[int]] = list_of_lists.copy()
print(new_lists_of_lists)

new_lists_of_lists[1][1] = 100
print(list_of_lists)
print(new_lists_of_lists)

print(id(list_of_lists[1]))
print(id(new_lists_of_lists[1]))  # taki sam identyfikator


new_lists_of_lists[1][1] = 4

print("Lista list (copy):")

from copy import deepcopy
list_of_lists: list[list[int]] = [[1, 2], [3, 4]]
print(list_of_lists)
new_lists_of_lists: list[list[int]] = deepcopy(list_of_lists)
print(new_lists_of_lists)

new_lists_of_lists[1][1] = 100
print(list_of_lists)
print(new_lists_of_lists)

print(id(list_of_lists[1]))
print(id(new_lists_of_lists[1]))  # różne identyfikatory

my_list: list[int] = []
for i in range(10):
    my_list.append(i ** 2)  # dodaje element na końcu listy

print(my_list)
