"""
    Обновите форму регистрации из hw5/reg_form.py таким образом, чтобы:

    1. Все данные пользователей сохранялись в файл users.txt в любом формате.
    2. В файл errors.txt записывать все ошибочные либо не валидные вводы.
        (не валидный номер телефона, email и т.д.)
"""

import utilities.reg_form as reg_form


def main():
    user_phone = reg_form.get_phone_number()
    user_email = reg_form.get_email()
    user_password = reg_form.get_password()

    with open('user.txt', 'a') as f:
        f.write(f'User Phone: {user_phone}\nUser Email: {user_email}\npassword: {user_password}')


if __name__ == '__main__':
    main()
