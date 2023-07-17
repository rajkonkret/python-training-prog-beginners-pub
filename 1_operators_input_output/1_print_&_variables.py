# komentarz

print()
print("Hello", "world")

print("Mam", 5, "złotych")
print("Mam", 5, "złotych", sep=",")
print("Łamanie\nlinii")
print("Łamanie")
print("linii")

print("Nie będzie nowej linii", end="")
print("Nie będzie nowej linii")

print("Programuję\\ w\tPythonie")


a = 5
print(type(a))
b = 1.5
print(type(b))
name = "Paweł"
print(type(name))
a = "Jacek"  # Nie ma problemu, aby przypisac zmienna innego typu

c: int = 120  # typehint
c = "Jacek"  # Delikatna sugesta dla IDE, nei zmienia działania kodu
print(c)

big_string: str ="""To zajmuje
wiele
linii"""

print(big_string)

is_earth_flat: bool = False
is_python_dynamically_typed: bool = True
print(type(is_earth_flat))

print(None)
print(type(None))

a = 5
b = 3

print("a =", a)
print("b =", b)
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("7 / 2.0 =", 7 / 2.0)
print("7 // 2.5 =", 7 // 2.5)
print("7 % 2.5 =", 7 % 2.5)
print("5 ** 2 =", 5 ** 2)
print("5 ** 2.5 =", 5 ** 2.5)
print("5j + 10j + 2=", 5j + 10j + 2)
print(type(5j))
print("-5 << 1 =", -5 << 1)


