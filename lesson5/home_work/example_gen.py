"""
    Пример использования модулей random и string

    Программа выводит случайный спец-символ либо число.

    * можно делать выборку в цикле и конкатенировать все в одну строку,
    если нужно больше, чем 1 символ
"""

from random import choice
from string import digits, punctuation


def gen_random_symbol():
    string_ = punctuation + digits
    print(f'String: {choice(string_)}')


gen_random_symbol()
