# Dodaj odpowiednią metodę magiczną __neg__ do klasy MyVector tak, aby możliwa była następująca operacja:
from vectorclass import Vector


class MyVector(Vector):
    pass


vector: MyVector = MyVector(5, 10)
print(-vector)
assert (-vector).values == MyVector(-5, -10).values
