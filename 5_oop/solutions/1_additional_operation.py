# Dodaj odpowiednią metodę magiczną __neg__ do klasy MyVector tak, aby możliwa była następująca operacja:
from vectorclass import Vector


class MyVector(Vector):
    def __neg__(self):
        return self.__class__(*[-x for x in self.values])

    # Alternatywne rozwiązanie:
    # def __neg__(self):
    #     result = MyVector()
    #     result.values = tuple(-x for x in self.values)
    #     return result



vector: MyVector = MyVector() + 1
assert (-vector).values == MyVector(-1, -1).values
