
try:
    print("try")
except:
    print("except")
else:
    print("else")
finally:
    print("finally")

# raise ValueError # rzucanie wyjątku

try:
    raise ValueError
except ValueError:
    print("Something bad happened")

try:
    raise ValueError("Message")
except ValueError as e:
    print(e)

try:
    result = 10 / 0
except Exception as e:
    print("An error occured: ", e)

# try:
#     result = 10 / 0  # rzuca ZeroDivisionError
# except ValueError as e:
#     print("An error occured: ", e)

# try:
#     raise BaseException
# except Exception:
#     print("test")

try:
    result = 10 / 0
except ValueError as e:
    print("Value error occured: ", e)
except Exception as e:
    print("An error occured: ", e)


class TrainingError(Exception):
    pass


# raise TrainingError("I am new exception")  # i więcej nie trzeba, aby rzucić wyjątek

try:
    result = 10 / 0
except (OverflowError, ZeroDivisionError) as e:
    print("Error occured: ", e)
