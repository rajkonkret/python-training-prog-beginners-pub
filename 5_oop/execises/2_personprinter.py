# Uzupełnij klasę Person tak, aby kod wykonywał się zgodnie z komentarzami

import datetime


class Person:
    pass


data: list[str] = ["Jacek,Kowalski,18", "Anna,Nowak,35"]

people: list[Person] = []

people.append(Person("Kamil", "Kaniecki", 28))
for data_entry in data:
    people.append(Person.from_string(data_entry))  # metoda statyczna, która przyjmuje ciągi, jak powyżej a zwraca odpowiedni obiekt


for person in people:
    print(person)
# Wypisuje
# Kamil Kaniecki, 28
# Jacek Kowalski, 18
# Anna Nowak, 35

print(people[0].year_of_birth)  # wypisuje 2005

