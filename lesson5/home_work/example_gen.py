"""
    Пример использования модулей random и string

    Программа выводит случайный спец-символ либо число.

    * можно делать выборку в цикле и конкатенировать все в одну строку,
    если нужно больше, чем 1 символ
"""

import string
import random


def main():
    special_string = string.digits + string.punctuation
    special_char = random.choice(special_string)

    print(f'Special Char: {special_char}')


if __name__ == "__main__":
    main()

