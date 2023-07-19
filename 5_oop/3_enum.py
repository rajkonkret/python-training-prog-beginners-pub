from enum import Enum


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

for day in Weekday:
    print(day)
    print(day.name)
    print(day.value)
