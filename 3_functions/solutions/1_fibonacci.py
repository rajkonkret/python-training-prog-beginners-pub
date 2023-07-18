# 1. Napisz funkcję rekurencyjnie, która zwraca n-ty wyraz ciągu fibonacciego (jest to ciąg, którego każdy wyraz, to suma dwóch poprzednich).
# Przetestuj dekorator cache z modułu functools i porównaj czasy wykonania z nim i bez niego.

from functools import cache

import timeit


def fibonacci(n: int) -> int:
    if n in [0, 1]:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@cache
def fibonacci_cached(n: int) -> int:
    if n in [0, 1]:
        return 1
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


print(timeit.timeit(lambda: fibonacci(20), number=1000))
print(timeit.timeit(lambda: fibonacci_cached(20), number=1000))
