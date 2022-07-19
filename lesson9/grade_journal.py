"""
    Пользователь вводит количество студентов N.
    После чего вводит N строк, в которых записана фамилия и балл через пробел.

    Программа выводит список фамилий, отсортированный по их баллам по убыванию.

    Пример:

    [out] Введите количество студентов:
    [in]  3

    [out] Введите фамилию и балл:
    [in]  Иванов 87

    [out] Введите фамилию и балл:
    [in]  Смирнов 90

    [out] Введите фамилию и балл:
    [in]  Фролов 89

    [out]
        1. Смирнов
        2. Фролов
        3. Иванов
"""
import re


def enter_date():
    data = []
    quantity_student = int(input('Введите количество студентов: '))
    while quantity_student:
        quantity_student -= 1
        student = input('Введите фамилию и балл: ')
        data.append({'name': re.search(r'[a-zA-Zа-яА-ЯёЁ]+', student).group(),
                     'value': re.sub(r'\D', "", student)})
    return data


def generate_sorted_data(data: list):
    count = 0
    for x in sorted(data, key=lambda d: d['value'], reverse=True):
        count += 1
        x.update({'level': count})
        yield x


def main():
    for date_student in generate_sorted_data(enter_date()):
        print(f"{date_student['level']}. {date_student['name']}")



if __name__ == '__main__':
    main()
