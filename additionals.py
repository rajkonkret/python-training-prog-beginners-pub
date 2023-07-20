import pydantic


class Person(pydantic.BaseModel):
    name: str
    surname: str


print(Person(name="John", surname="Doe"))
if False:
    print(Person(name="John", surname=5))  # zostanie rzucony wyjątek przy próbie utworzenia obiektu


@pydantic.validate_call(validate_return=True)
def fun_pydantic(p: Person) -> int:
    return 5

fun_pydantic(Person(name="John", surname="Doe"))  # zostanie rzucony wyjątek przy próbie wywołania funkcji

