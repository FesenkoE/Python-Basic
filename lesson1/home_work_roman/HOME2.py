"""
    Программа принимает на ввод 4 числа.
    Необходимо сложить первые два и отдельно вторые два.
    Разделить первую сумму на вторую.
    Вывести результат на экран.
"""

a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
c = int(input('Enter number c: '))
d = int(input('Enter number d: '))

result = (a + b) / (c + d)
print('Result: ', result)
