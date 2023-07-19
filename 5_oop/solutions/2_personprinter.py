# Uzupełnij klasę Person tak, aby kod wykonywał się zgodnie z komentarzami

import datetime


class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age}"

    @property
    def year_of_birth(self):
        return datetime.date.today().year - self.age

    @staticmethod
    def from_string(string: str) -> 'Person':
        name, surname, age = string.split(',')
        return Person(name, surname, int(age))


data: list[str] = ["Jacek,Kowalski,18", "Anna,Nowak,35"]

people: list[Person] = []
people.append(Person("Kamil", "Kaniecki", 28))

for data_entry in data:
    people.append(Person.from_string(data_entry))  # metoda statyczna


for person in people:
    print(person)
# Wypisuje
# Jacek Kowalski, 18
# Anna Nowak, 35
# Kamil Kaniecki, 28

print(people[0].year_of_birth)  # wypisuje 1995

