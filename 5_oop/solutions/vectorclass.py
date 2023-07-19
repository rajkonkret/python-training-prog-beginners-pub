import math
from typing import Union


class Vector:
    def __init__(self, *args):
        """ Create a vector, example: v = Vector(1,2) """
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args

    def norm(self) -> float:
        """ Returns the norm (length, magnitude) of the vector """
        return math.sqrt(sum(x * x for x in self))

    def normalize(self) -> 'Vector':
        """ Returns a normalized unit vector """
        norm = self.norm()
        normed = tuple(x / norm for x in self)
        return self.__class__(*normed)

    def inner(self, vector) -> float:
        """ Returns the dot product (inner product) of self and another vector
        """
        if not isinstance(vector, Vector):
            raise ValueError('The dot product requires another vector')
        return sum(a * b for a, b in zip(self, vector))

    def __mul__(self, other) -> Union['Vector', float]:
        """ Returns the dot product of self and other if multiplied
            by another Vector.  If multiplied by an int or float,
            multiplies each component by other.
        """
        if isinstance(other, Vector):
            return self.inner(other)
        elif isinstance(other, (int, float)):
            product = tuple(a * other for a in self)
            return self.__class__(*product)
        else:
            raise ValueError("Multiplication with type {} not supported".format(type(other)))

    def __rmul__(self, other) -> Union['Vector', float]:
        """ Called if 4 * self for instance """
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Vector):
            divided = tuple(self[i] / other[i] for i in range(len(self)))
        elif isinstance(other, (int, float)):
            divided = tuple(a / other for a in self)
        else:
            raise ValueError("Division with type {} not supported".format(type(other)))

        return self.__class__(*divided)

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        if isinstance(other, Vector):
            added = tuple(a + b for a, b in zip(self, other))
        elif isinstance(other, (int, float)):
            added = tuple(a + other for a in self)
        else:
            raise ValueError("Addition with type {} not supported".format(type(other)))

        return self.__class__(*added)

    def __radd__(self, other):
        """ Called if 4 + self for instance """
        return self.__add__(other)

    def __sub__(self, other):
        """ Returns the vector difference of self and other """
        if isinstance(other, Vector):
            subbed = tuple(a - b for a, b in zip(self, other))
        elif isinstance(other, (int, float)):
            subbed = tuple(a - other for a in self)
        else:
            raise ValueError("Subtraction with type {} not supported".format(type(other)))

        return self.__class__(*subbed)

    def __rsub__(self, other):
        """ Called if 4 - self for instance """
        return self.__sub__(other)

    def __iter__(self):
        return self.values.__iter__()

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __str__(self):
        return self.values.__str__()


if __name__ == '__main__':
    vector: Vector = Vector() + 1
    print(vector)

