"""
Написать функцию hello, которая принимает аргумент name - строку с именем и
выводит принтом "Привет, {name}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""


def hello(name):
    return print("Привет", name)

print(hello("Andrei"))


def log_decorator(def_hello_name):
    def _name():
        print("Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        def_hello_name()
        print("Выполнено {func.__name__}")
    return _name()


@log_decorator
def new_hello():
    print(" Hello Andrei")