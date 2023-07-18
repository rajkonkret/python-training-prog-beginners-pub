numbers: list[int] = [5, 3, 12, -5, 4, -4]

print(numbers)

numbers_incremented: list[int] = []
for number in numbers:
    numbers_incremented.append(number + 1)

print(numbers_incremented)

# list comprehension
numbers_incremented = [x + 1 for x in numbers]
print(numbers_incremented)

print(numbers)

numbers_squared = [x ** 2 for x in numbers]
print(numbers_squared)

messages: list[str] = ["File not found", "Connection error"]
print([x.upper() for x in messages])

# set comprehension
numbers_incremented_set: set = {x + 1 for x in numbers}
print(numbers_incremented_set)

# dict comprehension
numbers_incremented_dict: dict = {x: x + 1 for x in numbers}
print(numbers_incremented_dict)

numbers_incremented_tuple = tuple(x + 1 for x in numbers)
print(numbers_incremented_tuple)

numbers_squared_less_than_10 = []
for number in numbers:
    if number < 10:
        numbers_squared_less_than_10.append(number ** 2)
print(numbers_squared_less_than_10)
print([x**2 for x in numbers if x < 10])  # list comprehension odpowiadające powyższej pętli


