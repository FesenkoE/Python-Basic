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


def main():
    student_amount = int(input('Enter student amount: '))
    data = []

    for i in range(student_amount):
        student_data = (input('Enter student name and his rate with SPACE: ')).split()
        data.append({
            'name': student_data[0],
            'rate': student_data[1]
        })

    sorted_data = sorted(data, key=lambda d: d["rate"], reverse=True)
    i = 1
    for value in sorted_data:
        print(f"{i}. {value['name']}")
        i += 1


if __name__ == '__main__':
    main()
