words: list[str] = ["cucumber", "brrrr", "python", "bird"]
words.sort(key=len)
assert words == ['bird', 'brrrr', 'python', 'cucumber']

# Rozwiązanie z użyciem lambdy i list comprehension
# words.sort(key=lambda word: len([char for char in word if char.lower() in "aeiouy"]))

def vowel_counter(word: str):
    return len([char for char in word if char.lower() in "aeiouy"])


words.sort(key=vowel_counter)
assert words == ['brrrr', 'bird', 'python', 'cucumber']
