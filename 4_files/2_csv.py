print("a|bcd|efg".split("|"))  # zwróci listę ["a", "bcd", "efg"]

with open("airtravel.csv", "r") as file:
    header: str = file.readline()
    data: list[tuple] = []
    for line in file:
        values = line.strip().split(",")
        if len(values) == 4:
            data.append((values[0], int(values[1]), int(values[2]), int(values[3])))

print(data)

import numpy as np

data: np.ndarray = np.genfromtxt("airtravel.csv", encoding="utf-8",
                                 delimiter=',', skip_header=1, usecols=[1, 2, 3])

print(data)
print(data.shape)  # zwraca krotkę z wymiarami tablicy
print(data[:2])  # zwróci np.ndarray z 2 pierszymi wierszami
print(data[:, 1:])  # zwróci np.ndarray bez pierwszej kolumny
print(np.mean(data[:2]))  # zwróci średnią ze wszystkich wartości z dwóch pierwszych wierszy
print(data[:2])
print(data[:2] + 1)  # + 1 do np.ndarray zwróci tablicę z wszystkimi elementacmi powiększonymi o 1

import pandas as pd

data: pd.DataFrame = pd.read_csv("airtravel.csv")
print(data)
data_indexed = data.set_index("Month")
print(data_indexed)
print(data_indexed.columns)
print(data_indexed["1958"].mean())
print(data_indexed.loc["JAN"])
print(data_indexed.iloc[0])
print(data_indexed.iloc[0:2])
print(data_indexed["1958"] - data_indexed["1959"])


