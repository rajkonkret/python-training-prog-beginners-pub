import pydantic


class Person(pydantic.BaseModel):
    name: str
    surname: str


print(Person(name="John", surname="Doe"))
if False:
    print(Person(name="John", surname=5))  # zostanie rzucony wyjątek przy próbie utworzenia obiektu


@pydantic.validate_call
def fun_pydantic(p: Person):
    pass

fun_pydantic("a")  # zostanie rzucony wyjątek przy próbie wywołania funkcji

