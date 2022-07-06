"""
    Кортежи - неизменяемые списки, но могут содержать изменяемые элементы.

    Доступны методы списков count() и index()
"""

# Создание кортежа

tuple_1 = ()
tuple_2 = tuple("hello")

tuple_3 = (1, 2, 3)
tuple_4 = 1, 2, 3

print(tuple_1, tuple_2, tuple_3, tuple_4)
print(type(tuple_1), type(tuple_2), type(tuple_3), type(tuple_4))
