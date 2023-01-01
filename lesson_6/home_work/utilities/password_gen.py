"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 
    символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)

    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)


    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""

import string
import random


def choice_pwd():
    return input(
        '1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)\n'
        '2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)\n'
        '3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 '
        'до 16 символов)\n'
        '4. Сгенерировать пользовательский пароль ()\n'
    )


def pwd_len():
    pwd_length = int(input('Введите длину пароля: '))

    if pwd_length < 8:
        print('Пароль не надежный')

    return pwd_length


def simple_pwd():
    pwd = ''
    pwd_length = pwd_len()
    for i in range(pwd_length):
        pwd += random.choice(string.ascii_lowercase)

    return pwd


def medium_pwd():
    pwd = ''
    pwd_length = pwd_len()
    special_string = string.digits + string.ascii_letters

    for i in range(pwd_length):
        pwd += random.choice(special_string)

    return pwd


def strong_pwd():
    pwd = ''
    special_string = string.digits + string.ascii_letters + string.punctuation

    for i in range(random.randint(8, 16)):
        pwd += random.choice(special_string)

    if check_pwd(pwd):
        return pwd
    else:
        return strong_pwd()


def custom_pwd():
    pwd = ''
    special_string = input('Enter pool of chars: ').replace(' ', '')
    print(f'Special string: {special_string}')
    pwd_length = int(input('Enter password length: '))

    for i in range(pwd_length):
        pwd += random.choice(special_string)

    return pwd


def check_pwd(pwd):
    lower_char = False
    upper_char = False
    digit = False
    punctuation = False

    for char in pwd:
        if char.islower():
            lower_char = True
        elif char.isupper():
            upper_char = True
        elif char.isdigit():
            digit = True
        elif (not char.isnumeric()) and (not char.isdigit()):
            punctuation = True

    if lower_char and upper_char and digit and punctuation:
        return True

    return


if __name__ == '__main__':
    main()
