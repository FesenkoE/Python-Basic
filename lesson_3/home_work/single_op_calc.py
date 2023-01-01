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

while True:
    n = int(input('Enter number n: '))
    operation = input('Choice the operation (+, -, *, /): ')
    result = None

    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        result = int(input())
    else:
        print('Invalid operation!')
        continue

    if operation == '+':
        for i in range(n - 1):
            result += int(input())
    elif operation == '-':
        for i in range(n - 1):
            result -= int(input())
    elif operation == '*':
        for i in range(n - 1):
            result *= int(input())
    elif operation == '/':
        for i in range(n - 1):
            result += int(input())

    print('Result: ', result)

    answer = input('Continue? (y/n): ')

    if answer == 'n':
        print('Bye!')
        break
