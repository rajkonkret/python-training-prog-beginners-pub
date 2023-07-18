

def multiplier(number: float) -> float:
    """
    Multiplies argument number by 2
    :param number: numeric value
    :return: numeric value
    """
    return number * 2


def multiplier_3(number: float) -> float:
    """
    Multiplies argument by 3
    Args:
        number: numeric value

    Returns: multiplied numeric value

    """
    return number * 3

print(multiplier.__doc__)
print(multiplier_3.__doc__)

# aby wygenerować dokumentację w postaci html możemy użyć: python -m pydoc -w 5_docs
# alternatywnie: pdoc3 --html 5_docs (co wymaga instalacji: pip install pdoc3)
