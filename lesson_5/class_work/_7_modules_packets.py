"""
    Модуль - это файл с расширением .py
    Из модуля можно импортировать любые именованные объекты
    либо весь модуль целиком.

    Пакет - это набор модулей, которые содержаться в одной директории.
"""
from some_module_name import factorial

factorial()


# можно импортировать весь пакет целиком
import utils

# импорт модуля из пакета
from utils import functions

# импорт объектов из конкретного модуля
from utils.templates import HELLO_TEMPLATE, BYE_TEMPLATE

utils.functions.first_function()  # вызов функции из пакета

functions.second_function()  # вызов функции из модуля

name = input('What is your name? ')

print(HELLO_TEMPLATE.format(name=name))

input('Press Enter to exit..')

print(BYE_TEMPLATE.format(name=name))
