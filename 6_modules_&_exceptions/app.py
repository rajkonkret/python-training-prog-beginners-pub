import my_module

my_module.greeting_function("Hello")

from my_module import greeting_function

greeting_function("Hello")

from my_module import greeting_function as greeting

greeting("Hello")

from my_module import *  # zaimportuj wszystko, niekoniecznie zalecane

# python -m nazwa_modułu - uruchamia moduł o podanej nazwie

from module_directory import another_greeting

