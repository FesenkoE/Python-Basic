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
"""  # noqa: E501

import random
import string


def main():
    answer = input(
        '1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)\n'
        '2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)\n'
        '3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина \n'
        'от 8 до 16 символов)\n'
    )

    if answer == '1':
        pwd = simple_pass()
        print(f'Your simple password: {pwd}')
    elif answer == '2':
        pwd = middle_pass()
        print(f'Your middle password: {pwd}')
    elif answer == '3':
        pwd = strong_pass()
        print(f'Your strong password: {pwd}')
    else:
        print('Do correct choice!')
        main()


def simple_pass():
    pwd = ''
    for char in range(8):
        pwd += random.choice(string.ascii_lowercase)

    return pwd


def middle_pass():
    pwd = ''
    pwd_string = string.ascii_letters + string.digits
    for char in range(8):
        pwd += random.choice(pwd_string)

    return pwd


def strong_pass():
    pwd = ''
    pwd_string = string.ascii_letters + string.digits + string.punctuation

    for char in range(random.randint(8, 16)):
        pwd += random.choice(pwd_string)

    if check_pwd(pwd):
        return pwd

    return strong_pass()


def check_pwd(pwd):
    upper_letter = lower_letter = one_digit = spec_symbol = 0

    for char in pwd:
        if char.isupper():
            upper_letter += 1
        elif char.islower():
            lower_letter += 1
        elif char.isdigit():
            one_digit += 1
        else:
            spec_symbol += 1

    if upper_letter > 0 and lower_letter > 0 and one_digit > 0 and spec_symbol > 0:
        return True

    return False


if __name__ == '__main__':
    main()
