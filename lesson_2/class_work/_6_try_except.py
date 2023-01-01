"""
    try-except используется для перехвата исключений,
    чтоб программа не прекращала работу при возникновении ошибки.
"""

a = input('a = ')
b = input('b = ')

try:
    a = int(a)
    b = int(b)
    result = a / b
except ValueError:
    print(a, 'or', b, 'not an integer')
    print('not an integer')
except NameError:
    print('not defined')
except ZeroDivisionError:
    print('division by zero')
except Exception as e:
    print(e.__class__.__name__, ':', e)
else:
    # блок выполнится в том случае, если не было сгенерировано исключение
    print(result)
finally:
    # блок выполнится в любом случае
    print('finally')
