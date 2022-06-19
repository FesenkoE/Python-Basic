"""
    Пример использования модулей random и string

    Программа выводит случайный спец-символ либо число.

    * можно делать выборку в цикле и конкатенировать все в одну строку,
    если нужно больше, чем 1 символ
"""

import string
import random


def main():
    print(get_symbol_or_digit())


def get_symbol_or_digit(len_=1):
    symbol_and_digit = string.punctuation + string.digits
    res = ''

    for i in range(len_):
        res += random.choice(symbol_and_digit)

    return res
# return ''.join(random.sample(symbol_and_digit, len_))  # второй вариант, sample выводит список символов


if __name__ == '__main__':
    main()
