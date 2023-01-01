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
import utilities.password_gen as pwd_gen


def main():
    pwd = get_pwd()
    counter = 1

    while not check_pwd(pwd) and counter < 5:
        print('Insecure password')
        counter += 1
        pwd = get_pwd()

    if counter < 5:
        with open('password_gen_v2.txt', 'a') as f:
            f.write(pwd + '\n')
    else:
        print('Limit less than five! Bye!!!')
        return


def get_pwd():
    pwd_type = pwd_gen.choice_pwd()

    if pwd_type == '1':
        pwd = pwd_gen.simple_pwd()
    elif pwd_type == '2':
        pwd = pwd_gen.medium_pwd()
    elif pwd_type == '3':
        pwd = pwd_gen.strong_pwd()
    elif pwd_type == '4':
        pwd = pwd_gen.custom_pwd()
    else:
        print('Invalid number')
        return get_pwd()

    return pwd


def check_pwd(pwd):
    with open('password_gen_v2.txt', 'a+') as f:
        f.seek(0)
        for line in f:
            if pwd == line.replace('\n', ''):
                return False

        return True


if __name__ == '__main__':
    main()
