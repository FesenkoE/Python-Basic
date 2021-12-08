"""
    Необходимо написать простой калькулятор,
    который оперирует с двумя числами и оператором.

    В зависимости от введенного оператора,
    между числами проводится определенная операция.

    Результат выводится на экран.

    * обработать все возможные ошибки программы с помощью try-except
"""
result = 0

try:
    num_1 = int(input('Enter first number: '))
    operation = input('Enter operation (+ - * /): ')
    num_2 = int(input('Enter second number: '))

    if operation == '+':
        result = num_1 + num_2
    elif operation == '-':
        result = num_1 - num_2
    elif operation == '*':
        result = num_1 * num_2
    elif operation == '/':
        result = num_1 / num_2
    else:
        result = 'Unknown operation!'
except ValueError:
    print('Not a number')
except ZeroDivisionError:
    print('Division by zero')

print('result: ', result)






