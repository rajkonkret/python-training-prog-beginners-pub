# Mamy tutaj 2 przykłady kodu z pętlą. Zmodyfikuj go tak, aby zastąpić ją odpowiednim wyrażeniem, jak np. list comprehension.
# Pierwszy fragment
words: list[str] = ["python", "SnAkE", "function"]
print([word.upper() for word in words])


# Drugi fragment
numbers: list[int] = [1, 5, 7, 12, 33]
print("is_any_even =", any(number % 2 == 0 for number in numbers))
