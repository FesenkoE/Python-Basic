"""
    Продолжение и доп примеры декораторов из lesson9/_5_decorators.py

    Дано функции hello и bye.

    Необходимо реализовать функционал, чтоб сообщения, выводимые функциями
    оборачивалось в html теги:

    [in]
        hello('Max')
    [out]
        <html>
        Hello, Max!
        </html>

    [in]
        bye('John')
    [out]
        <p>
        Bye, John!
        </p>

"""


def hello(name):
    print(f"Hello, {name}!")


def bye(name):
    print(f"Bye, {name}!")


# 1. Как реализовать харкодом (так делать не нужно)

print("<html>")
hello("Max")
print("</html>")

print("<p>")
bye("John")
print("</p>")

# В таком случае для каждого оборачивания вызова функции нужно дописывать код
# и если нужно будет изменить название тега, нужно изменить несколько строк


# 2. Реализовать дополнительные функции декораторы, которые будут
# внутри себя оборачивать вызов нужной функции в тег.
# По сути, перенесем строки 36-38 и 40-42 в функции-декораторы


def html_decorator(func):
    def wrapper(name):
        print("<html>")
        func(name)
        print("</html>")

    return wrapper


def p_decorator(func):
    def wrapper(name):
        print("<p>")
        func(name)
        print("</p>")

    return wrapper


# Теперь можно задекорировать нужные функции и они будут оборачиваться тегом
@html_decorator
def hello(name):
    print(f"Hello, {name}!")


@p_decorator
def bye(name):
    print(f"Bye, {name}!")


# Теперь функцию можно просто вызывать, она расширится кодом декоратора
hello("Max")
bye("John")

# Результат такой же, как и в 1 варианте, но более универсальный и правильный
# Также, теперь можно комбинировать декораторы, например


@html_decorator
@p_decorator
def say_name(name):
    print(f"My name is {name}!")


say_name("Alex")

# Результат будет такой:
# <html>
# <p>
# My name is Alex!
# </p>
# </html>


# Как работает декоратор ???

# При вызове задекорированной функции происходит следующее
# Сначала вызывается функция-декоратор, в которую
# как аргумент передается задекорированная функция
# и результат пристаивается переменной с таким же именем.


def show_name(name):
    print(name)


print(show_name.__name__)

show_name = html_decorator(show_name)

# Декоратор возвращает ссылку на вложенную в него функцию, ее можно вызвать
# т.е. по сути show_name - это ссылка на функцию wrapper из декоратора

show_name("Max")

# <html>
# Max
# </html>

print(show_name.__name__)  # wrapper
