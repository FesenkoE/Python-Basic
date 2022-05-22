"""
    Вводится число от 1 до 999
    (если введено не число либо число вне диапазона - вывести сообщение)

    1. Найти сумму цифр числа.
    2. Вывести на экран, порядок, в котором расположены цифры числа
        (возростание/убывание/в разброс(равны))
"""
try:
    number = int(input('Enter number from 1 to 999: '))
    res = None
    order = None

    if 1 < number < 10:
        res = number
        order = 'Only one digit'
    elif 9 < number < 100:
        num_1 = number // 10
        num_2 = number % 10
        res = num_1 + num_2

        if num_1 > num_2:
            order = 'Reduce'
        elif num_1 < num_2:
            order = 'Decrease'
        else:
            order = 'The digits are equal'
    elif 99 < number < 1000:
        num_1 = number // 100
        num_2 = (number % 100) // 10
        num_3 = (number % 100) % 10

        res = num_1 + num_2 + num_3

        if num_1 > num_2 > num_3:
            order = 'Decrease'
        elif num_1 < num_2 < num_3:
            order = 'Reduce'
        else:
            order = 'Random or equal'
    else:
        print('Number less 1 or more than 999')
except ValueError:
    print('Not a number')
except Exception as e:
    print(e.__class__.__name__, ':', e)
else:
    print('Result: ', res)
    print('Order: ', order)
