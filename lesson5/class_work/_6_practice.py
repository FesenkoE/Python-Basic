"""
    Написать функцию capitalize, которая
    возводит 1 букву строки в верхний регистр, а все остальные в нижний.

    # ''.capitalize()
    # 'hello world' >> 'Hello world'
    # 'hello WoRld' >> 'Hello world'
    # 'HeLLo WoRld' >> 'Hello world'
"""


def capitalize(string):
    return string[0].upper() + string[1:].lower()


print(capitalize('hello world'))  # 'Hello world'
print(capitalize('hello WoRld'))  # 'Hello world'
print(capitalize('HeLLo WoRld'))  # 'Hello world'


"""
    Написать функцию, которая возводит число a в степень b.
"""


"""
    Написать функцию, которая по аналогии с вычисление факториала
    считает сумму числового рядо от 1 до n
"""
