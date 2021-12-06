"""
    Программа принимает на ввод 4 числа.
    Необходимо сложить первые два и отдельно вторые два.
    Разделить первую сумму на вторую.
    Вывести результат на экран.
"""

print('Enter 4 numbers:')
a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = ((a + b) / (c + d))
print('result: ', result)


