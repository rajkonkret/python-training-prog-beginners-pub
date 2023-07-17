
training_attendants: list[str] = ["Łukasz", "Marcin", "Maciek", "Paulina"]

who_will_pass_test: list[str] = ["Maciek", "Staszek", "Paulina"]

print(who_will_pass_test[0] in training_attendants)
print(who_will_pass_test[1] in training_attendants)
print(who_will_pass_test[2] in training_attendants)

# Pętla while
n: int = len(who_will_pass_test)
i: int = 0
while i < n:
    attendant: str = who_will_pass_test[i]
    if attendant in training_attendants:
        print(f"{attendant} zaliczy test")
    else:
        print(f"{attendant} nie znajduje się na liście {training_attendants}!")
    i += 1  # w pythonie nie ma i++

# Pętla for z użyciem range
n: int = len(who_will_pass_test)
for i in range(n):
    attendant: str = who_will_pass_test[i]
    if attendant in training_attendants:
        print(f"{attendant} zaliczy test")
    else:
        print(f"{attendant} nie znajduje się na liście {training_attendants}!")


# Pętla for na liście (for-each)
for attendant in who_will_pass_test:
    if attendant in training_attendants:
        print(f"{attendant} zaliczy test")
    else:
        print(f"{attendant} nie znajduje się na liście {training_attendants}!")

print(range(5))  # zwróci generator
print(list(range(5)))  # aby wyciągnąć z niego wartości można np. użyć list
print(list(range(2,5)))  # liczby od 2 do 5 (bez 5)
print(list(range(2,10,2)))  # # liczby od 2 do 10 (bez 10) co 2

# enumerate
for i, attendant in enumerate(who_will_pass_test):
    if attendant in training_attendants:
        print(f"{i}. {attendant} zaliczy test")
    else:
        print(f"{i}. {attendant} nie znajduje się na liście {training_attendants}!")

#  Podkreślnik wstawia się często w miejsce, gdzie przypisujemy wartość zmiennej, ale z tej zmiennej nie korzytamy
for _ in range(5):
    print("Hello")  # To się po prostu wykona 5 razy
