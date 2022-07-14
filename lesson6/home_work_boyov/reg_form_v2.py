"""
    Обновите форму регистрации из hw5/reg_form.py таким образом, чтобы:

    1. Все данные пользователей сохранялись в файл users.txt в любом формате.
    2. В файл errors.txt записывать все ошибочные либо не валидные вводы.
        (не валидный номер телефона, email и т.д.)
"""

# Решение в lesson8/register/main.py

from pathlib import Path
import reg_form
FILES_DIR = Path(__file__).resolve().parent / 'files'


def set_phone():

    phone = input('Введите номер телефона: ')
    if (res := reg_form.phone_format(phone))[0]:
        return res[1]
    else:
        print(res)
        save_error(res[1])
        return set_phone()


def set_email():
    """
    Пользователь вводит email.
    Программа проверяет валидность email:
    - должен иметь длину 6 символов и больше
        (функция len())
    - содержать один символ '@'
        (строчный метод count())
    - ** содержать логин и полный домен (логин@полный.домен)
    Пользователь может вводить email до тех пор, пока он не будет валидным.
    :return: str
    """

    email_ = input("Введите Ваш email: ")
    if reg_form.check_email(email_):
        return email_
    else:
        save_error(email_ + ' НЕ ВАЛИДНЫЙ EMAIL')
        print('НЕ ВАЛИДНЫЙ EMAIL')
        return set_email()


def set_password():
    """
    3. Пользователь ввод пароль.
    Программа проверяет надежность пароля:
    - минимум 8 символов
        (функция len())
    - пароль не должен содержать пробельные символы
        (строчный метод isspace())
    - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
        (строчные методы isupper(), islower(), isdigit())
    - ** наличие минимум 1 спец символа

    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
    Если подтверждение пароля не сходится с введенным паролем,
    то возвращаемся к пункту 3.
    :return: str
    """

    password = input("Пароль не должен содержать пробелы.\n"
                     "Должны быть минимум по одному символу в верхнем и нижнем регистре.\n"
                     "Должны быть минимум одна цифра.\n"
                     "Введите пароль: ")
    if (res := reg_form.check_password(password))[0]:
        return password
    else:
        save_error(password + res[1])
        return set_password()


def create_file_reg():
    try:
        with open(FILES_DIR / 'users.txt') as f:
            pass
    except FileNotFoundError:
        with open(FILES_DIR / 'users.txt', 'w') as f:
            f.write(f'PHONE / EMAIL / PASSWORD\n')


def save_error(value):
    with open(FILES_DIR / 'errors.txt', 'a') as f:
        f.write(value + '\n')


def save_new_user():
    with open(FILES_DIR / 'users.txt', 'a') as f:
        f.write(f'{set_phone()} / {set_email()} / {set_password()}\n')


def main():
    create_file_reg()
    save_new_user()


if __name__ == "__main__":
    main()
