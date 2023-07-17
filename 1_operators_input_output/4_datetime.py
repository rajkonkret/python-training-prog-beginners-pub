from datetime import date, datetime, timedelta

print(date.today())
print(type(date.today()))
print(datetime.now())
print(type(datetime.now()))
print(datetime.now().time())
print(type(datetime.now().time()))

print(date(2012, 1, 1))
print(date(year=2012, month=1, day=1))

# Jaki mamu jutro dzień?
today: date = date.today()
# print(today + 1)  # to nie zadziała

print(date(today.year, today.month, today.day + 1))  # Można w ten sposób
print(today + timedelta(days=1))
