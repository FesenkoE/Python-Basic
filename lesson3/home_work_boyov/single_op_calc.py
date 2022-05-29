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
    try:
        a = int(input('n: '))
        action = input('action: ')
        count = 0
        res = None

        while count < a:
            count += 1
            num = float(input('num: '))

            if action == '/':
                res = num if res is None else res / num
            elif action == '*':
                res = num if res is None else res * num
            elif action == '-':
                res = num if res is None else res - num
            elif action == '+':
                res = num if res is None else res + num
            else:
                print('Non-existent operator!')
                break
            print(res)

    except ValueError:
        print('Not valid value')
    except ZeroDivisionError:
        print('Division by zero is not possible!')

    y_n = input('Continue (Y/n)?')
    if y_n == 'n':
        print('Bye')
        break
    else:
        print('__________________\n')
