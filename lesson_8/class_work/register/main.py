"""
    1. Реализовать форму регистрации. (hw5)
    2 (3). Хранить данные пользователей на протяжении сеанса.
    3 (2). Сохранять данные пользователей в файл. (hw6)
    4. Покрыть код тестамы.
    5. Залить код в репозиторий GitHub.
"""
import re

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def main():
    user_list = []

    while True:
        phone = get_phone()
        email = get_email()
        password = get_password()

        user_list.append([phone, email, password])
        save_data(phone, email, password)

        print(
            f"\nПоздравляем с успешной регистрацией!"
            f"\nВаш номер телефона: +{phone}"
            f"\nВаш email: {email}"
            f'\nВаш пароль: {"*"*len(password)}'
        )

        if input("Continue? (Y/n)") == "n":
            break

    print(user_list)
    user_data = user_list[0]
    print(user_data[0], user_data[1], user_data[2])

    with open(BASE_DIR / "users.txt", "a") as f:
        for phone, email, password in user_list:
            print(f"{phone} {email} {password}", file=f)


def save_data(phone, email, password):
    with open(BASE_DIR / "users.txt", "a") as f:
        print(f"{phone} {email} {password}", file=f)


def formatted_phone(phone):
    phone = "".join(s for s in phone if s.isdigit())
    return "380" + phone[-9:]


def phone_valid(phone):
    if len(phone) == 12 and phone.isdigit():
        return True
    return False


def get_phone():
    phone = input("Enter phone number:")
    phone = formatted_phone(phone)

    if phone_valid(phone) is True:
        return phone
    return get_phone()


def get_email():
    email = input("Введите email: ")
    if len(email) < 6 or email.count("@") != 1 or email.startswith("@"):
        print("Неверный формат. Повторите ввод.")
        return get_email()
    return email


def get_password():
    password = input("Введите пароль: ")
    if len(password) < 8 or re.findall(r"\s", password):
        print("Пароль слишком простой. Придумайте более надежный пароль.")
        return get_password()

    u_counter = l_counter = d_counter = s_counter = 0
    for i in password:
        if i.isupper():
            u_counter += 1
        elif i.islower():
            l_counter += 1
        elif i.isdigit():
            d_counter += 1
        else:
            s_counter += 1

    if min(u_counter, l_counter, d_counter, s_counter) == 0:
        print("Пароль слишком простой. Придумайте более надежный пароль.")
        return get_password()

    if input("Повторите пароль: ") != password:
        print("Пароли не совпадают.")
        return get_password()
    return password


if __name__ == "__main__":
    main()
