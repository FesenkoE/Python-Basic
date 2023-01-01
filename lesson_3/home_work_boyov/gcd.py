"""
    Алгоритм Евклида. НОД - наибольший общий делитель

    1. Большее число делим на меньшее.
    2. Если делится без остатка, то меньшее число и есть НОД (выходим из цикла)
    3. Если есть остаток, то большее число заменяем на остаток от деления.
    4. Переходим к 1 пункту.

"""

while True:
    try:
        a = int(input('num first: '))
        b = int(input('num second: '))

        if a < 0 or b < 0:
            a = abs(a)
            b = abs(b)
            print('значения взяты по модулю')

        while True:
            if a < b:
                a, b = b, a

            if a % b == 0:
                nod = b
                print(nod)
                break
            else:
                a = a % b
    except ValueError:
        print('не верное значение')

    except ZeroDivisionError:
        print('рассматриваемые значения не должны быть "0"')
