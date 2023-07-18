# Wersja podstawowa:
# Napisz funkcję, która przyjmuje dowolną liczbę > 0 argumentów numerycznych i zwraca średnią arytmetyczną z nich.
# Wersja rozbudowana:
# Jeżeli podamy dodatkowy keyword argument "mean_type" o wartości "geo" to zamiast średniej arytmetycznej zostanie policzona
# średnia geometryczna, czyli pierwiastek n-tego stopnia z iloczynu n liczb.
# Wskazówka: pierwiastek n-tego stopnia można liczyć jako potęgowanie do 1/n.

def mean_calculator(*numbers, mean_type="arithmetic") -> float:
    n: int = len(numbers)
    if mean_type == "geo":
        product: float = 1
        for number in numbers:
            product *= number
        return product ** (1/n)
    return sum(numbers) / n


assert mean_calculator(1) == 1
assert mean_calculator(3, 2, 4) == 3
assert mean_calculator(1.5, 9, 4.5, 5) == 5
assert mean_calculator(1, mean_type="geo") == 1
assert mean_calculator(1, 9, mean_type="geo") == 3
assert mean_calculator(1, 1, 1, 20736, mean_type="geo") == 12
