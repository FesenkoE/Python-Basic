"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) данные владельцев,
    чьи имена начинаются на букву "m" либо заканчиваются на "а"
    (регистр не имеет значения).

    В файл записывать данные в таком формате:
    1. +380501234561 - Имя
    2. +380501234562 - Имя
    3. +380501234563 - Имя
    4. +380501234564 - Имя
"""
from pathlib import Path
from utilities.phone_format import get_phone_number

FILES_DIR = Path(__file__).resolve().parent / "files"


def main():
    with open(FILES_DIR / 'phone_book.txt', 'r') as f:
        for line in f:
            name = get_name(line)

            if name[0].lower() == 'm' or name[-1].lower() == 'a':
                phone_number = get_phone_number(line)
                write_contact(phone_number, name)
            else:
                continue


def get_name(line):
    name = ''

    for char in line:
        if char.isalpha():
            name += char

    return name.capitalize()


def write_contact(phone_number, name):
    with open(FILES_DIR / 'edited_phone_book.txt', 'a') as f:
        f.write(f'{phone_number} - {name}\n')


if __name__ == "__main__":
    main()
