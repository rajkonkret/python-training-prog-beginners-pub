# krotka (ang. tuple)

names: tuple[str, str, str] = ("Ania", "Jacek", "Agatka")

print(type(names))
# names[0] = "Marian" # To nie zadziała
print(names[0])
print(names[:2])  # krotki wspierają też slicing

for name in names:
    print(name)

print(list(names))
