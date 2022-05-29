"""
    (1-3 пункты были решены на уроке, необходимо привести все к нужному виду)

    При запуске программы выбор:
    1. Найти количество четных и нечетных цифр числа.
    2. Найти факториал числа.
    3. Вывести последовательность чисел в степени до предела.
    4. Выход.

    * после выполнения пунктов 1-3 попадаем обратно в меню.
"""

while True:
    print('1. Найти количество четных и нечетных цифр числа - введите "1"')
    print('2. Найти факториал числа - введите "2"')
    print('3. Вывести последовательность чисел в степени до предела - введите "3"')
    try:
        op = int(input('Выберете действие которое необходимо выполнить: '))

        if op == 1:
            num = int(input('Введите число: '))
            even = 0  # для четных
            odd = 0  # для нечетных
            while num > 0:
                last_digit = num % 10
                if last_digit % 2 == 0:
                    even += 1
                else:
                    odd += 1
                num //= 10
            print('чет:', even)
            print('нечет:', odd)
        elif op == 2:
            num = abs(int(input('Введите целое, положительное число: ')))
            factorial = 1
            while num > 1:
                factorial *= num
                num -= 1
            print(factorial)

        elif op == 3:
            limit = int(input('Введите предел: '))
            deg = int(input('Введите степень: '))
            res = 0
            count = 0
            while True:
                res = count ** deg
                count += 1
                if res <= limit:
                    print(res)
                else:
                    break
        else:
            print('Несуществующий оператор')
    except ValueError:
        print('Не допустимое значение')

    finish = input('Хотите продолжить(Y/n)? :')

    if finish == 'n':
        break
