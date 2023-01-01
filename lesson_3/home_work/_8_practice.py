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
    print('1. Найти количество четных и нечетных цифр числа.')
    print('2. Найти факториал числа.')
    print('3. Вывести последовательность чисел в степени до предела.')
    print('4. Выход.')

    choice = int(input('Сделайте выбор: '))

    if choice == 1:
        number = int(input("Введите число: "))
        even = 0
        odd = 0

        while number > 0:
            last_digit = number % 10

            if last_digit % 2 == 0:
                even += 1
            else:
                odd += 1

            number //= 10

        print("even:", even)
        print("odd:", odd)
        print('')
    elif choice == 2:
        number = int(input("Введите число: "))

        factorial = 1
        while number > 1:
            factorial *= number
            number -= 1

        print(factorial)
    elif choice == 3:
        limit = int(input("Предел: "))
        number = 1

        while (result := number ** 2) < limit:
            print(result)
            number += 1
    elif choice == 4:
        break
    else:
        print('Вы ввели неверное число!')

