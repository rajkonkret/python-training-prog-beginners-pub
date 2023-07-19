# Dodaj odpowiednią metodę magiczną __neg__ do klasy MyVector tak, aby możliwa była następująca operacja:
from vectorclass import Vector


class MyVector(Vector):
    def __neg__(self):
        return self.__class__(*[-x for x in self.values])


vector: MyVector = MyVector() + 1
assert (-vector).values == MyVector(-1, -1).values
