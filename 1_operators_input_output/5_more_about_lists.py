my_list: list[int] = [1, 5, 19, -3]

my_list.remove(5)  # usunie element o wartości podanej jako argument
print(my_list)  # [1, 19, -3]

print(my_list.pop(2))  # usuwa element o indeksie podanym jako argument i zwraca go

print(my_list)  # [1, 19]

del my_list[0]  # usuwa element o indelsie 0

print(my_list)  # [19]
