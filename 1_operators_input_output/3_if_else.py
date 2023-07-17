number: int = 4

if number % 2 == 0:
    print(f"Liczba {number} jest parzysta")
    print("Hello")

number = 5

if number % 2 != 0:
    print(f"Liczba {number} jest nieparzysta")

is_python_known_by_you: bool = True

if is_python_known_by_you:
    print("Gratulacje")
else:
    print("Zapraszam na szkolenie")

print(bool(1))
print(bool(0))
print(bool("test"))
print(bool(""))

string: str = "test"

if string:  # zostanie zmienna skonwertowana do typu bool
    print("String nie jest pusty")

if len(string) != 0:
    print("String nie jest pusty")

income_in_pln: int = 1_030_500

tax: float

if income_in_pln < 30_000:
    tax = 0
elif income_in_pln < 120_000:
    tax = income_in_pln * 0.12 - 3_600
else:
    tax = 10_800 + (income_in_pln - 120_000) * 0.32

print(f"Podatek od dochodu {income_in_pln}zł wynosi: {tax}zł")

password: str = "very_secret" * 10  # str * int zwielokrotni wartość str
print(password)
password_length: int = len(password)

if 4 <= password_length and 20 >= password_length:
    print("Hasło zaakceptowane")
else:
    print(f"Hasło ma długość {password_length}. "
          f"Powinno być z przedziału [4, 20]")

if 4 <= password_length <= 20:  # zadziała tak samo jak if 4 <= password_length and 20 >= password_length
    print("Hasło zaakceptowane")
else:
    print(f"Hasło ma długość {password_length}. "
          f"Powinno być z przedziału [4, 20]")

print(True or False)
print(True and False)

# match-case dostępne od pythona 3.8
print("Witaj w instalatorze programu X.")
menu_option: int = 0
print(f"Wybrano opcję {menu_option}")

match menu_option:
    case 0:
        print("Instalacja programu...")
    case 1:
        print("Sprawdzenie poprawności instalacji...")
    case 2:
        print("Deinstalacja programu...")
    case other:
        print(f"Nieznana opcja {other}")
