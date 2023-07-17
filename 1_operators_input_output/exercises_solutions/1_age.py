# Napisz program, który wczytuje od użytkownika rok urodzenia. Jeżeli wiek użytkownika mieści się między
# age_minimal, a age_maximal włącznie, to jest wyświetlany komunikat "access granted". W przeciwnym wypadku
# użytkownik otrzymuje komunikat "access denied".

from datetime import date

age_minimal: int = 18
age_maximal: int = 120

current_year: int = date.today().year
year_of_birth: int = int(input("Put year of birth: "))
age: int = current_year - year_of_birth

if age_minimal <= age <= age_maximal:
    print("Access granted")
else:
    print("Access denied")

