import time
from functools import cache


def add(a, b):
    return a + b


print(add(10, 2))

# wyrażenie lambda
add = lambda a, b: a + b

print(add(10, 2))

taxpayers = [(1336, "Jacek", "Kaniecki", 1570.13),
             (2422, "Anna", "Wiśniewska", 1443.28),
             (6334, "Marcel", "Nowak", 333.12),
             (112, "Karolina", "Szyndler", 578.13),
             (2148, "Jacek", "Doba", 112.10)]

print(max(taxpayers, key=lambda x: x[3]))  # zwróci nam krotkę o największym elemencie o indeksie 3

print(abs(-100))
print(max([1, 5, -3, 14, -150], key=abs))  # zwróci element o największej wartość bezwzględnej

print(max([1, 5, -3, 14, -150],
          key=lambda x: abs(x) if x > 0 else 0))  # zwróci element o największej wartość bezwzględnej


# generatory

def natural_numbers_generator(start: int, end: int = None):
    if end is not None:
        while start < end:
            yield start
            start += 1
    else:
        while True:
            yield start
            start += 1


my_generator = natural_numbers_generator(5)
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(list(natural_numbers_generator(5, 10)))


def factorial(n: int) -> int:
    if n == 0:
        return 1
    time.sleep(0.1)
    return n * factorial(n - 1)


print(factorial(10))


@cache
def factorial_cached(n: int) -> int:
    if n == 0:
        return 1
    time.sleep(0.1)
    return n * factorial_cached(n - 1)


print(factorial_cached(10))
print(factorial_cached(10))
print(factorial_cached(11))
print(factorial_cached.cache_info())
