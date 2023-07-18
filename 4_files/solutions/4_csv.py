# Wczytaj plik data.csv zawierający dane osób. Oblicz BMI dla każdej osoby
# (masa dzielona przez wzrost_w_metrach_do_kwadratu), średnią tych wartości i wypisz je na standardowe wyjście.

import numpy as np

data: np.ndarray = np.genfromtxt("data.csv", dtype=None, delimiter=',', encoding='utf-8', skip_header=1)

bmi_ndarray: np.ndarray = data[:, 3] / (data[:, 2] / 100) ** 2

for person, bmi in zip(data[:, 0], bmi_ndarray):
    print(f"Osoba o id {person} ma bmi {bmi:.2f}")

print(bmi_ndarray.mean())
