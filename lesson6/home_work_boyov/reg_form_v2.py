"""
    Обновите форму регистрации из hw5/reg_form.py таким образом, чтобы:

    1. Все данные пользователей сохранялись в файл users.txt в любом формате.
    2. В файл errors.txt записывать все ошибочные либо не валидные вводы.
        (не валидный номер телефона, email и т.д.)
"""

# Решение в lesson8/register/main.py

from pathlib import Path

FILES_DIR = Path(__file__).resolve().parent / 'files'


def set_phone():
    while True:
        phone = input('Enter phone number: ')
        phone_num = ''
        for char in phone:
            if char.isdigit():
                phone_num += char
        if len(phone_num) >= 9:
            phone_num = '380' + phone_num[-9::]
            return phone_num
        else:
            print('НЕ ВАЛИДНЫЙ НОМЕР')
            save_error(phone + ' НЕ ВАЛИДНЫЙ НОМЕР')
            continue


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
    while True:
        email_ = input("Введите Ваш email: ")
        if email_.count('@') != 1 \
                or len(email_[:email_.index('@')]) < 2 \
                or email_[email_.index('@'):].count('.') == 0:
            # пояснение второй проверки: последние 4 символа это минимум "@_._".
            # из чего следует, логин должен быть минимум 2 символа, тогда общая длина выйдет min 6 символов.
            # проверяем длину среза от 0 до индекса "@", должнпа быть не менее 2
            # третья проверка: берем срез начиная с "@" - доконца, считаем в нем колл-во ".". не должно быть нулем.
            # из устных разъямнений задачи...
            print('Введен не валидный email')
            save_error(email_ + ' НЕ ВАЛИДНЫЙ EMAIL')
        else:
            return email_


def  set_password():
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
    while True:
        password = input("Пароль не должен содержать пробелы.\n"
                         "Должны быть минимум по одному символу в верхнем и нижнем регистре.\n"
                         "Должны быть минимум одна цифра.\n"
                         "Введите пароль: ")
        flag_apper = 0
        flag_lower = 0
        flag_digit = 0
        flag_space = 0
        for char in password:
            if char.isupper():
                flag_apper = 1
            if char.islower():
                flag_lower = 1
            if char.isdigit():
                flag_digit = 1
            if char.isspace():
                flag_space = 1
        if len(password) < 8:
            print('КОРОТКИЙ ПАРОЛЬ')
            save_error(password + ' КОРОТКИЙ ПАРОЛЬ')
            continue
        elif not flag_apper or not flag_lower or not flag_digit:
            print('НЕ НАДЕЖНЫЙ ПАРОЛЬ')
            save_error(password + ' НЕ НАДЕЖНЫЙ ПАРОЛЬ')
            continue
        elif flag_space:
            print('ПАРОЛЬ СОДЕРЖИТ ПРОБЕЛЫ')
            save_error(password + ' ПАРОЛЬ СОДЕРЖИТ ПРОБЕЛЫ')
            continue
        else:
            password_reply = input('Повторите пароль: ')
            if password_reply == password:
                return password
            else:
                print('ПАРОЛИ НЕ СОВПОДАЮТ')
                save_error(password + ' ПАРОЛИ НЕ СОВПОДАЮТ')


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
