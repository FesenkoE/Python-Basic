"""
    1. Вывести на экран квадраты натуральных чисел не превыщающие limit.

    Например:
    Предел: 25
    1
    4
    9
    16
"""

limit = int(input("Предел: "))
number = 1

while (result := number ** 2) < limit:
    print(result)
    number += 1


"""
    2. Вывести на экран последовательность чисел
    начиная от 1 в степени p до заданного предела limit

    Например:
    степень 2, предел 25
    1
    4
    9
    16
"""

p = int(input("Введите степень: "))
limit = int(input("Предел: "))
number = 1

while (result := number ** p) < limit:
    print(result)
    number += 1
