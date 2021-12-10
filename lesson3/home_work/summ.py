"""
    Пользователь вводит начало и конец числового ряда.
    Если начало не введено - считать, что это 0.

    1. Программа считает и выводит на экран сумму числового ряда.
    2. Произведение нечетных чисел числового ряда.

    * обработать возможные ошибки
"""
try:
    start = int(input('Enter start: '))
    end = int(input('Enter end: '))
except ValueError:
    print('Enter a number')
else:
    start = start if start else 0
    sum_ = 0
    multiple = 1

    for i in range(start, end + 1):
        sum_ += i

        if i % 2 != 0:
            multiple *= i

    print('Summa: ', sum_)
    print('Multiple: ', multiple)

