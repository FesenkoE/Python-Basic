"""
    Вводится число от 1 до 999
    (если введено не число либо число вне диапазона - вывести сообщение)

    1. Найти сумму цифр числа.
    2. Вывести на экран, порядок, в котором расположены цифры числа
        (возростание/убывание/в разброс(равны))
"""

try:
    num = int(input('Enter integer from 1 to 999: '))
    if (num >= 1) and (num <= 999):
        a = num % 10
        num = num // 10
        b = num % 10
        c = num // 10
        sum_ = a + b + c
        if (a > b) and (b > c):
            print('Возрастание, сумма =', sum_)
        elif (a < b) and (b < c):
            print('Убывание, сумма =', sum_)
        else:
            print('Разброс(равны), сумма =', sum_)
    else:
        print('Number  out of range')
except:
    print('Not valid number')
