"""
    Магическое число.
    Необходимо угадать загаданное число за наименьшее количество попыток.

    Алгоритм:
    1. Генерируется случайное число.
    2. Пользователь вводит число.
    3. Если введенное число больше или меньше сгенерированного, то
        выводится соответствующее сообщение и возвращаемся к пункту 2.
    4. Иначе введенное число равняется сгенерированному -
        пользователь угадал число. Выводится само число и количество попыток.
        А так же вопрос "Continue? (Y/n) ".
    6. Если пользователь выбирает продолжить -
        обнуляем счетчик попыток и переходим к пункту 1.
    7. Иначе выводим сообщение 'Bye!'.

    * Для генерации случайного числа используем random.randint(-inf, +inf),
        где -inf - +inf - диапазон возможных чисел

    ** по желанию, можете хранить рекордное число попыток
    и сообщать пользователю, если он поставил новый рекорд
"""

import random

random_number = random.randint(1, 100)

answer = 'y'
record = 0
counter = 0

while answer != 'n':
    counter += 1
    number = int(input('Enter a number: '))

    if number > random_number:
        print('random number is less!')
    elif number < random_number:
        print('random number is more!')
    else:
        if counter < record or record == 0:
            record = counter

        print('Success! Magic number is: ', random_number)
        print('You guessed with ', counter, ' attempts')
        print('Record is: ', record)
        answer = input('Continue? (Y/n): ')

        if answer != 'n':
            random_number = random.randint(1, 100)
            counter = 0



