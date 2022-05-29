"""
    Пользователь вводит начало и конец числового ряда.
    Если начало не введено - считать, что это 0.

    1. Программа считает и выводит на экран сумму числового ряда.
    2. Произведение нечетных чисел числового ряда.

    * обработать возможные ошибки
"""

try:
    first_num = int(input('enter first num:'))
except ValueError:
    first_num = 0
try:
    final_num = int(input('enter final num:'))
except ValueError:
    final_num = 0

if first_num > final_num:  # если первое значение больше второго - меняем местами, иначе range  не сработает
    first_num, final_num = final_num, first_num

sum_ = 0
multi_odd = 0

for i in range(first_num, final_num + 1):
    sum_ += i
    if i % 2 != 0 and i != 0:
        if multi_odd == 0:  # при инициализации multi_odd присваивать 1 нельзя, т.к. при дипазоне (0, 0) multi_odd будет 1, что неверно
            multi_odd = 1
        multi_odd *= i

print('sum_ =', sum_, '\nmultiply odd =', multi_odd)


