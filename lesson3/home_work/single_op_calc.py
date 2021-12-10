"""
    Программа считает сумму/разницу/произведение/частное n чисел.
    Алгоритм:
    1. Пользователь вводит число n.
    2. Затем выбирает операцию (+, -, *, /).
    3. После этого вводит n чисел.
    4. Программа выводит результат и сообщение "Continue? (y/n)".
    5. Если пользователь вводит y, то программа выполняется сначала.
        Иначе - выводит сообщение 'Bye!' и прекращает свою работу.
"""

answer = 'y'

while answer != 'n':
    number = int(input('Enter a number: '))
    operation = input('Choice an operation (+ - * /): ')
    n_numbers = int(input('Enter n numbers: '))
    counter = 0
    result = number

    if operation == '+':
        for _ in range(n_numbers - 1):
            result += number
    elif operation == '-':
        for _ in range(n_numbers - 1):
            result -= number
    elif operation == '*':
        for _ in range(n_numbers - 1):
            result *= number
    elif operation == '/':
        for _ in range(n_numbers - 1):
            result /= number

    print('Result: ', result)

    answer = input('Continue Y/n: ')

    if answer == 'n':
        print('Bye')

