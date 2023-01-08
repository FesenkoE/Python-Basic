"""
    Для примера прктичекого применения декораторов представлено
    решение hw6/password_gen_v2.py с их использованием.
"""
from pathlib import Path
from random import choice, randint
from string import ascii_letters, digits, punctuation

BASE_DIR = Path(__file__).resolve().parent


def password_exists_decorator(func):
    """ Декоратор, который принимает функцию """

    def wrapper(*args, **kwargs):
        """ Обертка, в которой вызывается задекорированная функция"""

        password = func(*args, **kwargs)  # здесь вызывается функция
        with open(BASE_DIR / "passwords.txt", "a+") as f:
            f.seek(0)
            if password not in f.read():
                # Если пароля нет в файле - записываем в файл и возвращаем его
                print(password, file=f)
                return password

        # Если входим в бесконечную рекурсию,
        # значит уникальные пароли закончились и возвращаем None
        try:
            return wrapper(*args, **kwargs)
        except RecursionError:
            return None

    return wrapper


def main():
    user_choice = input(
        "1. Сгенерировать простой пароль\n"
        "2. Сгенерировать средний пароль\n"
        "3. Сгенерировать сложный пароль\n"
        "(сделайте выбор и нажмите Enter) "
    )

    if user_choice == "1":
        # для теста генерируем простой пароль из 2 символов
        password = password_gen("10", length=2)
    elif user_choice == "2":
        password = password_gen(ascii_letters + digits)
    elif user_choice == "3":
        password = strong_password_gen()
    else:
        return main()

    if password is None:
        print("\nЗакончились уникальные пароли :(")
    else:
        print("\nВаш пароль:", password)

    if input("\nСгенерировать еще? (Y/n) ") != "n":
        return main()


def base_password_gen(chars, length=8):
    """ Базовая не задекорированная функция, которая генерирует пароль """
    return "".join(choice(chars) for _ in range(length))


@password_exists_decorator
def password_gen(chars, length=8):
    """ Задекорированная функция для генерации простого/среднего пароля """
    return base_password_gen(chars, length)


@password_exists_decorator
def strong_password_gen():
    """ Задекорированная функция для генерации сложного пароля """
    length = randint(8, 16)
    password = base_password_gen(ascii_letters + digits + punctuation, length)
    l_counter = u_counter = d_counter = s_counter = 0
    for char in password:
        if char.islower():
            l_counter += 1
        elif char.isupper():
            u_counter += 1
        elif char.isdigit():
            d_counter += 1
        else:
            s_counter += 1

    if min(l_counter, u_counter, d_counter, s_counter) == 0:
        return strong_password_gen()
    return password


if __name__ == "__main__":
    main()
