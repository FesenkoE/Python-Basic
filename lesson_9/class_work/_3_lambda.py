"""
    lambda выражения

    lambda arg: return
"""


# классическая функция, которая возращает число x в квадрате
def pow_2(x):
    return x ** 2


# lambda функция, которая возвращает число x в квадрате
lambda_pow_2 = lambda x: x ** 2

print(pow_2(5))  # 25
print(lambda_pow_2(5))  # 25


# классическая функция, которая возвращает сумму 2х чисел
def summ(a, b):
    return a + b


# lambda функция, которая возвращает сумму 2х чисел
lambda_summ = lambda a, b: a + b

print(summ(5, 10))  # 15
print(lambda_summ(5, 10))  # 15
