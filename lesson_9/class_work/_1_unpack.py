"""
    Из 5 урока.

    Функция может принимать 0 и более позиционных и ключевых аргументов.

    *args в кортеж args запаковываются все позиционные аргументы
    **kwargs - в словарь kwargs запаковываются ключевые аргументы
"""


def func(*args, **kwargs):
    print(args)
    print(kwargs)


# после вызова данной функции с такими аргументами
func(1, 2, 3, 4, "python", 3.14, name="Max", surname="Smith")
# в args запакованы все позиционные аргументы - (1, 2, 3, 4, 'python', 3.14)
# в kwargs - ключевые в виде словаря {'name': 'Max', 'surname': 'Smith'}


"""
    Обратная операция - распаковка кортежей и словарей в функцию.
"""


def get_full_name(name, surname):
    return f"{name} {surname}"


# можно передавать распакованый кортеж в функцию
user_tuple = ("Max", "Smith")
get_full_name(*user_tuple)
# в моменте такого вызова в функцию попадают элементы кортежа, аналогично
get_full_name("Max", "Smith")


# так же можно распаковывать словарь
user_dict = {"name": "Jane", "surname": "Adams"}
get_full_name(**user_dict)
# в моменте такого вызова в функцию попадают ключи и значения, аналогично
get_full_name(name="Jane", surname="Adams")


# Еще примеры


def func(a, b, c):
    print(a)
    print(b)
    print(c)


my_tuple = (1, 2, 3)
a, b, c = my_tuple

# 3 варианта вызова функции с значениями кортежа my_tuple
func(a, b, c)
func(a=1, b=2, c=3)
func(*my_tuple)


# вызов функции с значениями словаря
my_dict = {"a": 1, "b": 2, "c": 3}

func(**my_dict)  # итог будет func(a=1, b=2, c=3)
