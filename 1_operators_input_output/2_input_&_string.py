# input() - służy do pobierania danych od użytkownika ze standardowego wejścia

# Wersja 1:
# a = input("Podaj liczbę a: ")
# b = input("Podaj liczbę b: ")
# print(type(a))
# print(type(b))
#
# print("a + b = ", a + b)


# Wersja 2:
# a: int = int(input("Podaj liczbę a: "))
# b: int = int(input("Podaj liczbę b: "))
# print(type(a))
# print(type(b))
#
# print("a + b = ", a + b)

# # Wersja 3
# a: float = float(input("Podaj liczbę a: "))
# b: float = float(input("Podaj liczbę b: "))
# print(type(a))
# print(type(b))
#
# print("a + b = ", a / b)

# Wersja 4
a: float = float(input("Podaj liczbę a: "))
b: float = float(input("Podaj liczbę b: "))
result: float = a / b
print(f"{a} / {b} = {result:.3f}")  # f -string (dostępny od pythona 3.6)
print("{} / {} = {:.3f}".format(a, b, result))

