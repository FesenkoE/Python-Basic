"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой

    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран

    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt

    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое

    5.
    В средину файла file_practice.txt вставить строку " *some inserted text* "
    (средина - имеется в виду средина текста)
"""

from pathlib import Path


def main():
    home_work_folder = Path(__file__).resolve().parent
    text_txt = home_work_folder / 'files/text.txt'

    with open(home_work_folder / 'file_practice.txt', 'w+') as f:
        f.write('Starting practice with files\n')
        f.seek(0)
        data = f.read(5)
        print(data.upper())
        f.seek(0)
        print(f.read())

    with open(text_txt, 'r+') as f:
        data = f.read()

        e_count = data.count('e')
        i_count = data.count('i')

        if e_count > i_count:
            new_data = data.replace('i', 'e')
        else:
            new_data = data.replace('e', 'i')

        with open(home_work_folder / 'file_practice.txt', 'w+') as practice_f:
            practice_f.write(new_data)

    with open(home_work_folder / 'file_practice.txt', 'r+') as f:
        data = f.read()

        if len(data) % 2 == 0:
            f.write('\nthe end')
        else:
            f.write('\nbye')

        f.seek(0)
        data = f.read()
        print(data)

    first_part = data[:int(len(data) / 2)]
    second_part = ' *some inserted text* '
    third_part = data[int(len(data) / 2):]
    new_data = first_part + second_part + third_part

    with open(home_work_folder / 'file_practice.txt', 'w+') as f:
        f.write(new_data)


if __name__ == '__main__':
    main()
