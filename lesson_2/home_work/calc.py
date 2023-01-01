"""
    Необходимо написать простой калькулятор,
    который оперирует с двумя числами и оператором.

    В зависимости от введенного оператора,
    между числами проводится определенная операция.

    Результат выводится на экран.

    * обработать все возможные ошибки программы с помощью try-except
"""

try:
    result = None
    num_a = int(input('Enter number a: '))
    operation = input('Enter operation (+ - * /): ')
    num_b = int(input('Enter number b: '))

    if operation == '+':
        result = num_a + num_b
    elif operation == '-':
        result = num_a - num_b
    elif operation == '*':
        result = num_a * num_b
    elif operation == '/':
        result = num_a / num_b
    else:
        print('Invalid operation')
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Division by Zero')
except Exception as e:
    print(e.__class__.__name__, ':', e)
else:
    print('Result:', result)
finally:
    print('The End')






