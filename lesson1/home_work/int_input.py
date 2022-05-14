"""
    Программа принимает на ввод 4 числа.
    Необходимо сложить первые два и отдельно вторые два.
    Разделить первую сумму на вторую.
    Вывести результат на экран.
"""

num_1 = int(input('Enter num_1: '))
num_2 = int(input('Enter num_2: '))
num_3 = int(input('Enter num_3: '))
num_4 = int(input('Enter num_4: '))

result = (num_1 + num_2) / (num_3 + num_4)
print(result)

