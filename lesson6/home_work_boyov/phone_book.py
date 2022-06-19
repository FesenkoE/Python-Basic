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
import re

FILES_DIR = Path(__file__).resolve().parent / "files"


def phone_format(phone_num):
#    for char in phone_num:
#        if not char.isdigit():
#            phone_num = phone_num.replace(char, '')  # удаляем лишние символы
    if len(phone_num) >= 9:
        return '+380' + phone_num[-9::]
    else:
        return phone_num



def main():
    counter = 0
    with open(FILES_DIR / 'phone_book.txt') as f:
        for line in f.readlines():
            name = re.search(r"\w+", line)
            name = name.group().capitalize()
            if re.search(r'\bM', name) or re.search(r'a\b', name):
                phone = re.sub(r'\D+', '', line)
                phone = phone_format(phone)
                print(name, phone)
                counter += 1
                with open(FILES_DIR / 'edited_phone_book.txt', 'a') as nf:
                    nf.write(f'{counter}. {phone} - {name}\n')


if __name__ == "__main__":
    main()
