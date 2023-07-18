# Mamy tutaj 2 przykłady kodu z pętlą.
# Zmodyfikuj go tak, aby zastąpić ją odpowiednim wyrażeniem, jak np. list comprehension.
# Pierwszy fragment
words: list[str] = ["python", "SnAkE", "function"]
i: int = 0
upper_case_words = []
while i < len(words):
    upper_case_words.append(words[i].upper())
    i += 1
print(upper_case_words)


# Drugi fragment
numbers: list[int] = [1, 5, 7, 12, 33]
is_any_even: bool = False
for number in numbers:
    if number % 2 == 0:
        is_any_even = True
    i += 1
print("is_any_even =", is_any_even)
