"""
    Вводится число от 1 до 999
    (если введено не число либо число вне диапазона - вывести сообщение)

    1. Найти сумму цифр числа.
    2. Вывести на экран, порядок, в котором расположены цифры числа
        (возростание/убывание/в разброс(равны))
"""
sum_ = 0

try:
    number = int(input('Enter a number: '))
except ValueError:
    print('Not a number')
else:
    if 0 < number < 10:
        sum_ = number
    elif 9 < number < 100:
        sum_ = number // 10 + number % 10
    elif 99 < number < 1000:
        sum_ = number // 100 + (number % 100) // 10 + (number % 100) % 10
    else:
        print('Number is not in [0 - 999]')

print(f'Summa of numbers is: {sum_}')

