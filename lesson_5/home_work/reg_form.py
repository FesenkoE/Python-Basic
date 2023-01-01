"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.

    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)

    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер

    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.

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

    Программа выводит сообщение:

    Поздравляем с успешной регистрацией!
    Ваш номер телефона: +380501234567
    Ваш email: example@mail.com
    Ваш пароль: ********** (кол-во  == кол-ву символов пароля)

"""


def main():
    user_phone = get_phone_number()
    user_email = get_email()
    user_password = get_password()

    print('Поздравляем с успешной регистрацией!')
    print(f'Ваш номер телефона: {user_phone}')
    print(f'Ваш email: {user_email}')
    print(f'Ваш пароль: {user_password}')


def get_phone_number():
    phone_number = input('Enter phone number: ')
    prepare_phone_number = ''

    for digit in phone_number:
        if digit.isdigit():
            prepare_phone_number += digit

    if len(prepare_phone_number) < 10:
        return get_phone_number()
    else:
        phone_number = '+38' + prepare_phone_number[-9:]

    return phone_number


def get_email():
    email = input('Enter email: ')
    if check_email(email):
        return email
    else:
        return get_email()


def check_email(email):
    if len(email) > 5 and email.count('@') == 1:
        return True

    return


def get_password():
    user_password = input('Enter password: ')

    if check_password(user_password):
        user_repeat_password = input('Repeat password: ')

        if user_password == user_repeat_password:
            return user_password
        else:
            return get_password()
    else:
        return get_password()


def check_password(pwd):
    pwd_len = False
    pwd_is_space = False
    pwd_is_lower = False
    pwd_is_upper = False
    pwd_is_digit = False
    pwd_is_special_char = False

    if len(pwd) > 8 and not pwd.isspace():
        pwd_len = pwd_is_space = True

    for char in pwd:
        if char.islower():
            pwd_is_lower = True
        elif char.isupper():
            pwd_is_upper = True
        elif char.isdigit():
            pwd_is_digit = True
        elif (not char.isnumeric()) and (not char.isdigit()):
            pwd_is_special_char = True

    if pwd_len and pwd_is_space and pwd_is_lower and pwd_is_upper and pwd_is_digit and pwd_is_special_char:
        return True

    return


if __name__ == '__main__':
    main()
