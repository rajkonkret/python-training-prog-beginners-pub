numbers: list[int] = [1, 2, 5, -1, 10, 12]

print([x > 0 for x in numbers])
print(any([x > 0 for x in numbers]))
print(any(x > 0 for x in numbers))  # gdy którykolwiek element będzie True, to any zwróci True
print(all(x > 0 for x in numbers))  # gdy wszystkie elementy będą True, to all zwróci True
