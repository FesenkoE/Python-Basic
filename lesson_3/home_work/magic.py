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

random_number = random.randint(0, 100)
record = 0
attempt = 0

while True:
    number = int(input('Enter a number: '))
    attempt += 1

    if number < random_number:
        print('Random number more than your number')
    elif number > random_number:
        print('Random number less than your number')
    else:
        if not record or record > attempt:
            record = attempt

        print('You guessed random number - ', number)
        print('Attempt - ', attempt)
        print('Your record - ', record)

        answer = input('Continue? (Y/n) ')

        if answer != 'n':
            attempt = 0
            random_number = random.randint(0, 100)
        else:
            print('Bye!')
            break
