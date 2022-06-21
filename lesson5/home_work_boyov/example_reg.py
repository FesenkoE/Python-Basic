"""
    Пример использования рекурсии для формы регистрации.

    Допустим программа задает вопрос: Сколько будет 2 + 2?
    до тех пор, пока не получит правильный ответ,
    после чего выводит сообщение "Верно, 4!".

    Данную программу можно модифицировать, и для удобства пользователя
    выводить сообщение при неверном ответе.
"""

import random


def main():
    verification_question()


def verification_question():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    res = a + b
    answer = int(input(f'Сколько будет {a} + {b} = ?'))
    if answer != res:
        verification_question()
    else:
        print(f'Верно, {res}')


if __name__ == '__main__':
    main()
