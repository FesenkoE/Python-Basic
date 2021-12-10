"""
    Алгоритм Евклида. НОД - наибольший общий делитель

    1. Большее число делим на меньшее.
    2. Если делится без остатка, то меньшее число и есть НОД (выходим из цикла)
    3. Если есть остаток, то большее число заменяем на остаток от деления.
    4. Переходим к 1 пункту.

"""

num_a = int(input('Enter number A: '))
num_b = int(input('Enter number B: '))

while num_a != 0 and num_b != 0:
    if num_a > num_b:
        num_a = num_a % num_b
    else:
        num_b = num_b % num_a

print('Result: ', num_a + num_b)
