"""
    Ввести с помощью input() 3 числа.
    Вывести их с помощью print() в обратном порядке.

    Пример работы программы:

    Ввод:
    1
    125
    13

    Вывод:
    13
    125
    1
"""

print('Ввод:')
a = input()
b = input()
c = input()

print('\nВывод:')
print(c, b, a, sep='\n')
