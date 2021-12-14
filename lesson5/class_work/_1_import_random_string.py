"""
    Для импортирования сторонних модулей, библиотек используется:
    import module

    Для импортирования конкретной функции/константы из модуля:
    from module import some_function

    Импортируемому объкту можно задать псевдоним,
    под которым он будет исползоваться в коде
    from module import some_function as func

    Чтобы импортировать все объекты из модуля (не рекомендуется):
    from module import *

"""

import random

print(random.randint(1, 10))  # случайное число из диапазона от 1 до 10
print(random.choice('hello world'))  # случайный элемент из последовательности
print(random.sample('hello world', 2))  # случайная выборка 2 элементов

from random import randint as rint, choice

print(rint(1, 10))
print(choice('hello world'))

import string

print(string.ascii_letters)  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_lowercase)  # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase)  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.punctuation)  # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.digits)  # '0123456789'

from string import ascii_letters as letters

print(letters)  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
