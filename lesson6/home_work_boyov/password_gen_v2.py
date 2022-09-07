"""
    Обновите генератор паролей из hw5/password_gen.py таким образом, чтобы:

    1. Все сгенерированные пароли записывались в файл.
    2. После генерации пароля, сравнить его с содержимым файла.
        Если в файле уже записан такой пароль,
        то вывести сообщение с предупреждением "Insecure password".

    *3. Программа должна генерировать только уникальные пароли.
        Если в результате пункта 2 пароль уже содержится в файле, то генерируем
        его заново.

    * дополнительно стоит обрабатывать количество попыток генерации,
    так как после того, как будут сгенерированы все возможные комбинации,
    программа зациклится либо уйдет в бесконечную рекурсию и сломается

"""


import utilities.password_gen as p_g


def create_file():
    try:
        with open('password_gen_v2.txt') as f:
            pass
    except FileNotFoundError:
        with open('password_gen_v2.txt', 'w') as f:
            pass


def write_password_in_file(pwd):  # пароль не генериркется новый... куда я смотрел!? шо за тупоссть. переделать
    count = 0
    while count <= 10:
        password = pwd()
        with open('password_gen_v2.txt', 'r') as f:
            list_password = f.readlines()
        if password + '\n' not in list_password:
            with open('password_gen_v2.txt', 'a') as f:
                f.write(password + '\n')
            return password
        else:
            print("Insecure password")
            count += 1


def main():
    create_file()

    match p_g.choice_typ_password():
        case '1':
            return write_password_in_file(p_g.generate_password_low)
        case '2':
            return write_password_in_file(p_g.generate_password_letter_and_dig)
        case '3':
            return write_password_in_file(p_g.generate_password_strong)
        case '4':
            return write_password_in_file(p_g.generate_password_user)
        case _:
            print('Не существующий вариант')


if __name__ == "__main__":
    main()
