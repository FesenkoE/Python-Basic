"""
    Необходимо написать простой калькулятор,
    который оперирует с двумя числами и оператором.

    В зависимости от введенного оператора,
    между числами проводится определенная операция.

    Результат выводится на экран.

    * обработать все возможные ошибки программы с помощью try-except
"""

a = None
b = None
action = None
res = None

try:
    a = float(input('a: '))
    action = input('action: ')
    b = float(input('b: '))

    if action == '/':
        res = a / b
    elif action == '*':
        res = a * b
    elif action == '-':
        res = a - b
    elif action == '+':
        res = a + b
    else:
        print('Invalid operation')

except ValueError:
    print('Not valid value')
except ZeroDivisionError:
    print('Division by zero')
else:
    print('Result: ', res)
