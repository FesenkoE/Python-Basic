"""
    Алгоритм Евклида. НОД - наибольший общий делитель

    1. Большее число делим на меньшее.
    2. Если делится без остатка, то меньшее число и есть НОД (выходим из цикла)
    3. Если есть остаток, то большее число заменяем на остаток от деления.
    4. Переходим к 1 пункту.

"""

number_a = int(input('Enter number_a: '))
number_b = int(input('Enter number_b: '))

while True:
    if number_a > number_b:
        if number_a % number_b:
            number_a = number_a % number_b
        else:
            print(number_b)
            break
    else:
        if number_b % number_a:
            number_b = number_b % number_a
        else:
            print(number_a)
            break
